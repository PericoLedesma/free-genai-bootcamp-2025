
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

system_template = "Translate the following from English into {language}"






# ----------------------- Init the model ----------------------- #
model = init_chat_model(
    model="gpt-3.5-turbo",                 # Name of the model
    model_provider="openai",              # Provider (e.g., "openai", "azure", "anthropic")
    temperature=0.7,                       # Controls randomness (0 = deterministic, 1 = creative)
    max_tokens=1024,                       # Max number of tokens to generate
    timeout=60,                            # Request timeout in seconds
    streaming=False,                       # Whether to stream responses
)


print("Model:")
print(model)
print("-" * 20)
# ----------------------- Create the prompt ----------------------- #
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})
print("Prompt:")
print(prompt)
print("-" * 20)
# ----------------------- Invoke the model with the messages ----------------------- #
response = model.invoke(prompt)
print("Response:")
print(response.content)
print("-" * 20)

