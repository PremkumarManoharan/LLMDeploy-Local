import streamlit as st
import requests
import json

st.title("Kefihub Chatbot")

# Initialize chat history and suggested questions
if "messages" not in st.session_state:
    st.session_state.messages = []

if "suggested_questions" not in st.session_state:
    st.session_state.suggested_questions = [
        "What services does Kefihub offer?",
        "Tell me about your pricing model.",
        "Can you help me schedule a demo?",
        "What are the available time slots for a demo?"
    ]

# Function to update suggested questions
def update_suggested_questions():
    st.session_state.suggested_questions = [
        "What services does Kefihub offer?",
        "Tell me about your pricing model.",
        "Can you help me schedule a demo?",
        "What are the available time slots for a demo?",
        "Can you explain your cloud computing services?",
        "Tell me more about your Generative AI services."
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to stream API responses
def stream_chatbot_response(full_prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "agent",
        "prompt": full_prompt,
        "stream": True
    }
    response_content = ""
    with requests.post(url, json=data, stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    try:
                        json_line = json.loads(decoded_line)
                        if "response" in json_line:
                            response_content += json_line["response"]
                            yield response_content, False
                        if json_line.get("done"):
                            yield response_content, True
                            break
                    except json.JSONDecodeError:
                        continue
        else:
            st.write("Error:", response.status_code)
            st.write(response.text)

# Function to get the last 5 messages as context
def get_context():
    context = ""
    for msg in st.session_state.messages[-2:]:
        context += f"{msg['role'].capitalize()}: {msg['content']}\n"
    return context

# React to user input or selected suggested question
def handle_input(prompt):
    context = get_context()
    full_prompt = context + f"User: {prompt}\nAssistant:"

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Placeholder for assistant message
    response_placeholder = st.empty()
    response_text = ""
    is_done = False

    # Stream the response
    for partial_response, done in stream_chatbot_response(full_prompt):
        response_text = partial_response
        response_placeholder.markdown(f"**Assistant**: {response_text}")
        if done:
            is_done = True
            break
    
    # Add the final assistant response to chat history if done
    if is_done:
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        response_placeholder.empty()  # Clear the placeholder
        with st.chat_message("assistant"):
            st.markdown(response_text)
        # Update suggested questions
        update_suggested_questions()

# Input box for user prompts
if prompt := st.chat_input("What is up?"):
    handle_input(prompt)

# Display suggested questions
st.write("### Suggested Questions:")
for question in st.session_state.suggested_questions:
    if st.button(question):
        handle_input(question)
        st.experimental_rerun()
