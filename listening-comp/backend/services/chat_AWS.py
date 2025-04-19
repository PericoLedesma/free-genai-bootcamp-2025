import boto3
import json
import logging
from botocore.exceptions import ClientError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AWS_MODEL_ID = "amazon.titan-text-express-v1"
# AWS_MODEL_ID = "amazon.nova-micro-v1"

class AWSBedrockClient:
    """
    A client for interacting with AWS Bedrock's LLM models.
    """

    def __init__(self,
                 model_id=AWS_MODEL_ID,
                 region_name='eu-central-1'):
        print(f"Initializing AWSBedrockClient .....")
        self.model_id = model_id
        self.client = boto3.client(service_name='bedrock-runtime',
                                   region_name=region_name)

    def invoke_model(self, prompt):
        """
        Invokes the specified model with the supplied prompt.
        param brt: A bedrock runtime boto3 client
        param model_id: The model ID for the model that you want to use.
        param prompt: The prompt that you want to send to the model.

        :return: The text response from the model.
        """

        # Format the request payload using the model's native structure.
        native_request = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 512,
                "temperature": 0.5,
                "topP": 0.9
            }
        }

        # Convert the native request to JSON.
        request = json.dumps(native_request)

        try:
            # Invoke the model with the request.
            response = self.client.invoke_model(modelId=self.model_id, body=request)

            # Decode the response body.
            model_response = json.loads(response["body"].read())

            # Extract and print the response text.
            response_text = model_response["results"][0]["outputText"]
            return response_text

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{self.model_id}'. Reason: {e}")
            raise



if __name__ == "__main__":
    bedrock_client = AWSBedrockClient()
    prompt = "Describe the purpose of a 'hello world' program in one line."
    response = bedrock_client.invoke_model(prompt)
    print(f"Response: {response}")
    logger.info("Done.")

'''# New endpoint to talk to AWS Bedrock service
print("herre")
bedrock_client = AWSBedrockClient()

'''