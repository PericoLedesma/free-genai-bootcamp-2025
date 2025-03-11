import os
import requests

import openai
from openai import OpenAI




class OpenAIService:
    def __init__(self):
        self.client = OpenAI()

    def chat(self,
             prompt: str,
             model: str = "gpt-4o") -> str:

        # headers = {
        #     "Content-Type": "application/json",
        #     "x-api-key": self.api_key
        # }

        data = {
            "model": model,
            "prompt": prompt,
            "max_tokens_to_sample": 300
        }

        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print(completion.choices[0].message.content)
        # if completion.status_code == 200:
        #     result = completion.choices[0].message.content
        #     return result.get("completion", "No completion returned")
        # else:
        #     return f"Error: {response.status_code} {response.text}"




if __name__ == '__main__':
    service = OpenAIService()
    service.chat("Hello")


