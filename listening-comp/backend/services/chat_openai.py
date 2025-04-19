from openai import OpenAI


class ChatOpenAI:
    def __init__(self):
        print("Initializing ChatOpenAI client...")
        self.client = OpenAI()
        self.conversation = []  # This list will hold the conversation history

    def chat(self, prompt: str, model: str = "gpt-4o") -> str:
        # Add the user's message to the conversation history

        self.conversation.append({"role": "user", "content": prompt})

        # Send the entire conversation to the API
        completion = self.client.chat.completions.create(
            model=model,
            messages=self.conversation
        )
        response = completion.choices[0].message.content
        print(response)

        # Add the assistant's response to the conversation history
        self.conversation.append({"role": "assistant", "content": response})
        return response

    def stream_chat(self, prompt: str, model: str = "gpt-4o") -> None:
        self.conversation.append({"role": "user", "content": prompt})
        stream = self.client.chat.completions.create(
            model=model,
            messages=self.conversation,
            stream=True
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
        print()  # New line after streaming completes

        # (Optional) If you want to capture the full response in the conversation history,
        # you'll need to aggregate the streamed chunks into one complete response.

    def print_conversation(self) -> None:
        """Prints the entire conversation history."""
        for msg in self.conversation:
            print(f"{msg['role']}: {msg['content']}")


if __name__ == '__main__':
    chat_instance = ChatOpenAI()
    # Example usage: Regular chat
    print(chat_instance.chat("Hello, how are you?"))

    # Uncomment the following line to test streaming chat
    # chat_instance.stream_chat("Tell me a story.")
