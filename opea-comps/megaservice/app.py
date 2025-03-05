'''
Service orchestration framework using MicroService and ServiceOrchestrator, which are imported from comps.
•	MicroService: Represents an individual service (like an LLM service or an embedding service).
•	ServiceOrchestrator: Manages multiple microservices and their workflows.
•	ServiceType: Enum defining different types of services (e.g., LLM, Embedding).
'''

from comps import MicroService, ServiceOrchestrator
from comps import ServiceType
# from comps.cores.mega.constants import ServiceType

from comps import ServiceRoleType, MegaServiceEndpoint
from comps.cores.proto.api_protocol import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionResponseChoice,
    ChatMessage,
    UsageInfo,
)



import os
import requests

# EMBEDDING_SERVICE_HOST_IP = os.getenv("EMBEDDING_SERVICE_HOST_IP", "0.0.0.0")
# EMBEDDING_SERVICE_PORT = os.getenv("EMBEDDING_SERVICE_PORT", 6000)

# LLM_SERVICE_HOST_IP = os.getenv("LLM_SERVICE_HOST_IP", "0.0.0.0")
# LLM_SERVICE_PORT = os.getenv("LLM_SERVICE_PORT", 9000)

LLM_SERVICE_HOST_IP = "127.0.0.1"
LLM_SERVICE_PORT = 8088 #9000

MEGASERVICE_HOST = "127.0.0.1"
MEGASERVICE_PORT = 8000



class ExampleService:
    def __init__(self, host=MEGASERVICE_HOST, port=MEGASERVICE_PORT):
        self.host = host
        self.port = port
        self.megaservice = ServiceOrchestrator()
        # self.endpoint = str(MegaServiceEndpoint.CHAT)
        self.endpoint = "/v1/example-service"

    def add_remote_service(self):
        print("**Adding remote services...")
        # embedding = MicroService(
        #     name="embedding",
        #     host=EMBEDDING_SERVICE_HOST_IP,
        #     port=EMBEDDING_SERVICE_PORT,
        #     endpoint="/v1/embeddings",
        #     use_remote_service=True,
        #     service_type=ServiceType.EMBEDDING,
        # )
        llm = MicroService(
            name="llm",
            host=LLM_SERVICE_HOST_IP,
            port=LLM_SERVICE_PORT,
            endpoint="/v1/chat/completions",
            use_remote_service=True,
            service_type=ServiceType.LLM,
        )

        print(f"Configuring LLM service:")
        print(f"- Host: {LLM_SERVICE_HOST_IP}")
        print(f"- Port: {LLM_SERVICE_PORT}")
        print(f"- Endpoint: {llm.endpoint}")
        print(f"- Full URL: http://{LLM_SERVICE_HOST_IP}:{LLM_SERVICE_PORT}{llm.endpoint}")
        print(f"- Service Type: {llm.service_type}")

        # self.megaservice.add(embedding).add(llm)
        # self.megaservice.flow_to(embedding, llm)
        #
        self.megaservice.add(llm)
        # self.megaservice.flow_to(llm)
        print("**Remote services added**")

    def start(self):
        print("\n**Starting MEGA-Service...")
        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse,
        )


        self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])

        print(f"MEGA-Service configured with endpoint: {self.endpoint}")
        print("-" * 50)
        self.service.start()
        print("Service ended")

    async def handle_request(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        print("Request: ", request)
        try:
            # Schedule the request through the orchestrator
            result = await self.megaservice.schedule(request.dict())

            # Create the response
            response = ChatCompletionResponse(
                model=request.model or "example-model",
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        message=ChatMessage(
                            role="assistant",
                            content=str(result)  # Convert the result to string if it isn't already
                        ),
                        finish_reason="stop"
                    )
                ],
                usage=UsageInfo(
                    prompt_tokens=0,
                    completion_tokens=0,
                    total_tokens=0
                )
            )
            print("Response: ", response)
            return response
        except Exception as e:
            print("Respond Error: ", e)
            return ChatCompletionResponse(
                model=request.model or "example-model",
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        message=ChatMessage(
                            role="assistant",
                            content="Sorry, I encountered an error while processing your request."
                        ),
                        finish_reason="stop"
                    )
                ],
                usage=UsageInfo(
                    prompt_tokens=0,
                    completion_tokens=0,
                    total_tokens=0
                )
            )



if __name__ == "__main__":
    print('Runnning ...')
    example = ExampleService()
    example.add_remote_service()
    example.start()



