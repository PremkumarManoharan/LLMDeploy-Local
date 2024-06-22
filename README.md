# LLMDeploy-Local Overview

LLMDeploy-Local provides a method to run the Ollama large language model using Docker. This guide will help you set up and interact with the model locally.

## Running Ollama Using Docker

### Start the Docker Container

```sh
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### Access the Container

Exec into the running container to interact with the model.

### Run Llama3 Model

```sh
ollama run llama3
```

## Interacting with the Model

### Chat Example

```plaintext
>>> Hi what model do you use
```

I'm an AI, so I don't have a specific "model" in the classical sense. Instead, I'm a large language model trained on a massive dataset of text from various sources, including books, articles, and online content.

My training data is based on the BERT (Bidirectional Encoder Representations from Transformers) architecture, which is a popular neural network-based approach for natural language processing tasks. Specifically, my training data includes:

1. The entire Wikipedia corpus (~50 million articles)
2. BookCorpus, a dataset of 7,500 books
3. Common Crawl Web Corpus, a dataset of ~45 billion web pages
4. Other sources, including news articles, academic papers, and online forums

This massive training set allows me to learn patterns and relationships in language, enabling me to generate human-like text responses when interacting with users like you.

So, while I don't have a single "model" per se, I'm proud to be built on the robust BERT architecture and fueled by an enormous dataset of diverse text!

### Help Command

```plaintext
>>> /help
```

Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use `"""` to begin a multi-line message.

### Exit Chat

```plaintext
>>> /bye
```

## Creating and Running a Custom Agent

### Create a Modelfile

```sh
vi Modelfile
```

### Create and Run the Agent

```sh
ollama create agent -f ./Modelfile
ollama run agent
```

### Chat with Custom Bot

You can interact with your custom bot using the following curl command:

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?"
}'
```
