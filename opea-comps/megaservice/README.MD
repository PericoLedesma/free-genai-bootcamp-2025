# GenAIComps 

GenAIComps provides a suite of microservices, leveraging a service composer to assemble a mega-service tailored for real-world Enterprise AI applications.
All the microservices are containerized, allowing cloud native deployment.

https://opea-project.github.io/latest/GenAIComps/README.html
https://github.com/opea-project/GenAIComps


## Mega-service 
Service orchestration framework using MicroService and ServiceOrchestrator, which are imported from comps.
•	MicroService: Represents an individual service (like an LLM service or an embedding service).
•	ServiceOrchestrator: Manages multiple microservices and their workflows.
•	ServiceType: Enum defining different types of services (e.g., LLM, Embedding).

-  Generate request to the megaservice
```bash
    curl http://0.0.0.0:8000/v1/health_check 
    curl http://0.0.0.0:8000/health
    curl http://0.0.0.0:8000/v1/statistics

```

- endpoint = MegaServiceEndpoint.CHAT = "/v1/chat/completions" (check MegaServiceEndpoint for more endpoints)
```bash
curl http://0.0.0.0:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "messages": "What is the revenue of Nike in 2023?"
    }'
```

- endpoint of megaservice = "v1/example-service"
```bash
    curl http://0.0.0.0:8000/v1/example-service -d '{
      "model": "llama3.2:1B",
      "prompt": "Why is the sky blue?"
    }'
```





