import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import json


TRANSCRIPT_FOLDER = 'transcripts'
TRANSCRIPT_FOLDER = 'transcripts'
class StructuredData:
    def __init__(self, video_id):
        self.video_id = video_id
        self.transcript = self.read_transcript()
        self.llm = OpenAI()
        # print(self.llm.invoke("Hello how are you?"))


    def read_transcript(self):
        file_path = os.path.join(TRANSCRIPT_FOLDER, f'{self.video_id}.txt')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Transcript file '{file_path}' not found.")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            raise FileNotFoundError(f"Error reading file: '{file_path}' not found.")


    def structure_data(self):
        with open('services/structure_data_prompt.txt', 'r') as file:
            prompt_template = file.read()
        prompt = PromptTemplate.from_template(prompt_template)

        chain = prompt | self.llm

        response = chain.invoke({"transcript": self.transcript})
        print(response)
        return response





# ------------------------------------------------------ #
def lets_structure_data(video_id):
    print(f"Structuring data for video ID: {video_id}")
    struct_data_class = StructuredData(video_id)
    struct_data = struct_data_class.structure_data()

    return struct_data_class.transcript, struct_data




if __name__ == '__main__':
    lets_structure_data("test2")






