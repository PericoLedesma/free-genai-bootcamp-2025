import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import tiktoken

TRANSCRIPT_FOLDER = 'transcripts'


class StructuredData:
    def __init__(self, video_id):
        print(f"Initializing StructuredData class for video ID: {video_id}")
        self.video_id = video_id
        self.transcript = self.read_transcript()
        self.llm = init_chat_model(model="gpt-3.5-turbo",  # Name of the model
                                   model_provider="openai",  # Provider (e.g., "openai", "azure", "anthropic")
                                   temperature=0.7,  # Controls randomness (0 = deterministic, 1 = creative)
                                   max_tokens=4096,  # Max number of tokens to generate
                                   timeout=60,  # Request timeout in seconds
                                   streaming=False,  # Whether to stream responses
                                   )

        # print(f"\t LLM initialized: {self.llm}")

    def read_transcript(self):
        print(f"Reading transcript for video ID: {self.video_id}...")
        file_path = os.path.join(TRANSCRIPT_FOLDER, f'{self.video_id}.txt')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Transcript file '{file_path}' not found.")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            raise FileNotFoundError(f"Error reading file: '{file_path}' not found.")

    def prompt_template(self):
        try:
            with open('services/structure_data_prompt.txt', 'r') as file:
                prompt_template = file.read()
            return prompt_template
        except Exception as e:
            raise FileNotFoundError(f"Error reading prompt template: {e}")

    def structure_data(self):
        print(f"Structuring data for video ID: {self.video_id}...")

        prompt_template = ChatPromptTemplate.from_messages(
            [("system", self.prompt_template()), ("user", "{transcript}")]
        )

        prompt = prompt_template.invoke({"transcript": self.transcript})

        # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        # tokenized = encoding.encode(prompt.content)
        # token_count = len(tokenized)
        # print(f"Token count: {token_count}")
        print("-" * 50)
        try:
            response = self.llm.invoke(prompt)
        except Exception as e:
            raise RuntimeError(f"Error during LLM invocation: {e}")
        print(response.content)
        return response.content


# ------------------------------------------------------ #
def lets_structure_data(video_id):
    print(f"Structuring data for video ID: {video_id}")
    struct_data_class = StructuredData(video_id)
    struct_data = struct_data_class.structure_data()

    return struct_data_class.transcript, struct_data


if __name__ == '__main__':
    lets_structure_data("test2")
