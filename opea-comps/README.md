## Running Ollama Third-Party Service

### Choosing a moderl 
You can get the model id from the [Ollama Model library](https://ollama.com/library).


### Getting the Host IP
You can get the host IP by running the following command:
```bash
    sudo apt install net-tools
    ifconfig
```

Or you can try this way `$(hostname -I | awk '{print $1}')`



### Running the service
You can run the service by running the following command:
```bash
    LLM_ENDPOINT_PORT=8088 LLM_MODEL_ID="llama3.2:1b" host_ip=127.0.0.1 docker-compose up
```

NO_PROXY=localhost

## Ollama API
Once the service is up and running, you can make calls to the ollama API

https://github.com/ollama/ollama/blob/main/docs/api.md

### Pull the model 
```bash
    curl http://localhost:8088/api/pull -d '{
  "model": "llama3.2:1B"
}'
```

### Generate request
```bash
    curl http://127.0.0.1:8088/api/generate -d '{
      "model": "llama3.2:1B",
      "prompt": "Why is the sky blue?"
    }'
```