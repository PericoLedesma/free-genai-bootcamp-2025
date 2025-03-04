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
LLM_SERVICE_PORT = 8088


class ExampleService:
    def __init__(self, host="0.0.0.0", port=8000):
        self.host = host
        self.port = port
        self.megaservice = ServiceOrchestrator()
        # self.endpoint = str(MegaServiceEndpoint.CHAT)
        self.endpoint = "v1/example"

    def add_remote_service(self):
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
        # self.megaservice.add(embedding).add(llm)
        # self.megaservice.flow_to(embedding, llm)

    def start(self):
        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
                input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse,
        )

        self.megaservice = ServiceOrchestrator()
        self.endpoint = str(MegaServiceEndpoint.CHAT_QNA)


        # self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])
        self.service.add_route(self.endpoint, methods=["POST"])

        self.service.start()

if __name__ == "__main__":
    print('Starting service...')
    example = ExampleService()
    example.add_remote_service()
    example.start()
    print('Service started')



