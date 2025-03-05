# Running Ollama Third-Party Service

### LLM Serive
#### Choosing a moderl 
You can get the model id from the [Ollama Model library](https://ollama.com/library).


#### Getting the Host IP
You can get the host IP by running the following command:
```bash
    sudo apt install net-tools
    ifconfig
```

Or you can try this way `$(hostname -I | awk '{print $1}')`

#### Running the service
You can run the service by running the following command(without environment variables): #todo make default values
```bash
    docker-compose up
```

With the following environment variables: (pull model after
```bash
    LLM_ENDPOINT_PORT=9000 LLM_MODEL_ID="llama3.2:1b" host_ip=127.0.0.1 docker-compose up
    HOST_IP=$(hostname -I | awk '{print $1}') NO_PROXY=localhost LLM_ENDPOINT_PORT=9000 LLM_MODEL_ID="llama3.2:1b" docker compose up

```

#### Ollama API
Once the service is up and running, you can make calls to the ollama API

https://github.com/ollama/ollama/blob/main/docs/api.md

- Pull the model 
```bash
    curl http://localhost:9000/api/pull -d '{
  "model": "llama3.2:1B"
}'
```

- Generate request to the llm container
```bash
    curl http://127.0.0.1:9000/api/generate -d '{
      "model": "llama3.2:1B",
      "prompt": "Why is the sky blue?"
    }'
```

-  Generate request to the megaservice
```bash
    curl http://0.0.0.0:8000/v1/example-service -d '{
      "model": "llama3.2:1B",
      "prompt": "Why is the sky blue?"
    }'
```

-  Generate request to the megaservice
```bash
    curl http://0.0.0.0:8000/v1/health_check 
    curl http://0.0.0.0:8000/health
    curl http://0.0.0.0:8000/v1/statistics

```

```bash
curl -X POST http://localhost:8000/v1/example-service \
     -H "Content-Type: application/json" \
     -d '{
          "messages": "Hello, this is a test message"
     }'
```


# Technical Uncertainty
Q Does bridge mode mean we can only accses Ollama API with another model in the docker compose?
A No, the host machine will be able to access it

Q: Which port is being mapped 8008->141414
In this case 8008 is the port that host machine will access. the other other in the guest port (the port of the service inside container)

Q: If we pass the LLM_MODEL_Id to the ollama server will it download the model when on start?
It does not appear so. The ollama CLI might be running multiple APIs so you need to call the /pull api before trying to generat text

Q: Will the model be downloaded in the container? does that mean the ml model will be deleted when the container stops running?
A: The model will download into the container, and vanish when the container stop running. You need to mount a local drive and there is probably more work to be done.

Q: For LLM service which can text-generation it suggets it will only work with TGI/vLLM and all you have to do is have it running. Does TGI and vLLM have a stardarized API or is there code to detect which one is running? Do we have to really use Xeon or Guadi processor?
A:vLLM, TGI (Text Generation Inference), and Ollama all offer APIs with OpenAI compatibility, so in theory they should be interchangable.