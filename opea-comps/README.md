# Running Ollama Third-Party Service

## GenAIComps 

GenAIComps provides a suite of microservices, leveraging a service composer to assemble a mega-service tailored for real-world Enterprise AI applications.
All the microservices are containerized, allowing cloud native deployment.

https://opea-project.github.io/latest/GenAIComps/README.html
https://github.com/opea-project/GenAIComps

### Mega-service 
Service orchestration framework using MicroService and ServiceOrchestrator, which are imported from comps.
•	MicroService: Represents an individual service (like an LLM service or an embedding service).
•	ServiceOrchestrator: Manages multiple microservices and their workflows.
•	ServiceType: Enum defining different types of services (e.g., LLM, Embedding).

- endpoint = MegaServiceEndpoint.CHAT = "/v1/chat/completions" (check MegaServiceEndpoint for more endpoints)
```bash
curl http://0.0.0.0:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "messages": "What is the revenue of Nike in 2023?"
    }'
```

- - endpoint = "v1/example"
```bash
curl http://0.0.0.0:8000/v1/example\
    -H "Content-Type: application/json" \
    -d '{
        "messages": "What is the revenue of Nike in 2023?"
    }'
```



### LLM Serivec
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
You can run the service by running the following command(without environment variables):
```bash
    docker-compose up
```

With the following environment variables:
```bash
    docker-compose up
    LLM_ENDPOINT_PORT=8088 LLM_MODEL_ID="llama3.2:1b" host_ip=127.0.0.1 docker-compose up
```

NO_PROXY=localhost

#### Ollama API
Once the service is up and running, you can make calls to the ollama API

https://github.com/ollama/ollama/blob/main/docs/api.md

- Pull the model 
```bash
    curl http://localhost:8088/api/pull -d '{
  "model": "llama3.2:1B"
}'
```

- Generate request
```bash
    curl http://127.0.0.1:8088/api/generate -d '{
      "model": "llama3.2:1B",
      "prompt": "Why is the sky blue?"
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