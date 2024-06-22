# LLMDeploy-Local Overview

LLMDeploy-Local provides a method to run the Ollama large language model using Docker. This guide will help you set up and interact with the model locally.

[![Watch the video](https://img.youtube.com/vi/z_gv7HOLUmI/0.jpg)](https://www.youtube.com/watch?v=z_gv7HOLUmI)

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

## Advantages of Using Docker

Using Docker provides several benefits for deploying models like Ollama:

- **Isolation**: Docker containers run in isolation, ensuring that dependencies or settings within a container do not interfere with others.
- **Portability**: Containers can run consistently across any platform, from local development machines to production servers, as long as Docker is installed.
- **Scalability**: Docker makes it easy to scale applications up or down by simply starting more or fewer containers.
- **Efficiency**: Containers share the host system’s kernel, making them more efficient than virtual machines in terms of system resources.

## Creating and Running a Custom Agent

### Create a Modelfile

```sh
vi Modelfile
```

**Modelfile Content**

```Dockerfile
FROM llama3

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Customer Support for a Company called Kefihub. Answer as 'Agent Tina', the assistant, only.
"""
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

## Enhancement of the Custom Model

To enhance the custom model:
- **Data Tuning**: Continuously add and refine training datasets to improve accuracy and adapt to new topics or changing user needs.
- **Parameter Adjustment**: Experiment with different settings for parameters like `temperature` to find the optimal balance between creativity and coherence.
- **Feature Expansion**: Integrate additional functionalities, such as support for more languages or advanced context understanding.

## Deploying the Model in Kubernetes

Kubernetes offers a robust solution for deploying containerized applications like the Ollama model at scale:

1. **Container Orchestration**: Automates the deployment, scaling, and management of containerized applications.
2. **Service Discovery and Load Balancing**: Kubernetes can expose a container using a DNS name or its own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
3. **Self-healing**: Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and only advertises them to clients when they are ready to serve.
4. **Automated Rollouts and Rollbacks**: Kubernetes progressively rolls out changes to your application or its configuration, while monitoring application health to ensure it doesn’t kill all your instances at the same time. If something goes wrong, Kubernetes will rollback the change for you.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ollama
  template:
    metadata:
      labels:
        app: ollama
    spec:
      containers:
      - name: ollama
        image: ollama/ollama:latest
        ports:
        - containerPort: 11434
```

This YAML file defines a deployment that manages three replicas of the Ollama container, ensuring high availability and load balancing. I will continue adding steps to deploy the custom model completely into a kubernetes cluster
