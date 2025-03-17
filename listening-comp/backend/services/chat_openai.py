import os
import requests

import openai
from openai import OpenAI

def stream_chat(prompt: str,
                model: str = "gpt-4o") -> str:

    client = OpenAI()
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
        stream=True,
    )
    # Content print(chunk.choices[0].delta.content)
    # Finish with print(chunk.finish_reason) = stop else None
    for chunk in stream:
        print(chunk.choices[0].delta.content)



def chat(prompt: str, model: str = "gpt-4o") -> str:
    client = OpenAI()
    # headers = {
    #     "Content-Type": "application/json",
    #     "x-api-key": self.api_key
    # }

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content



 # -----------------------------------------------------------
if __name__ == '__main__':
    # chat("Hello")
    stream_chat()

