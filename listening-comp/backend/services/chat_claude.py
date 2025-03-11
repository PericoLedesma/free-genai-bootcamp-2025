import os
import requests

import openai
from openai import OpenAI
openai_api_key = os.environ.get("OPENAI_API_KEY")


# # Configuration: Set your Anthropic API key and endpoint.
# ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
# API_URL = "https://api.anthropic.com/v1/complete"
# MODEL = "claude-v1"  # Adjust to the appropriate model if needed.


class ClaudeService:
    def __init__(self):
        # self.api_key = os.getenv("CLAUDE_API_KEY")
        self.api_key = os.environ.get("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("Please set the CLAUDE_API_KEY environment variable")
        self.endpoint = "https://api.anthropic.com/v1/complete"

    def chat(self, prompt: str, model: str = "claude-v1") -> str:
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }
        data = {
            "model": model,
            "prompt": prompt,
            "max_tokens_to_sample": 300
        }
        response = requests.post(self.endpoint, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result.get("completion", "No completion returned")
        else:
            return f"Error: {response.status_code} {response.text}"



def chat_with_claude(prompt: str) -> dict:
    print("chat_with_claude")
    return {"response": "Claude's response goes here."}

    # headers = {
    #     "x-api-key": ANTHROPIC_API_KEY,
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "model": MODEL,
    #     "prompt": prompt,
    #     "max_tokens_to_sample": 200,  # Adjust based on your requirements.
    #     "stop_sequences": ["\n\nHuman:"]
    # }
    # response = requests.post(API_URL, headers=headers, json=data)
    # if response.ok:
    #     return response.json()
    # else:
    #     # Return error details if the request failed.
    #     return {"error": response.status_code, "message": response.text}




