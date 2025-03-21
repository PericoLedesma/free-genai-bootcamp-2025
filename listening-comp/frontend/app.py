import streamlit as st
import requests  # Import the requests library

BACKEND_URL = "http://127.0.0.1:8080"  # URL of the backend server

# Page configuration
st.set_page_config(
    page_title="German Learning Assistant",
    layout="wide",
)
chat_service = st.sidebar.radio(
    "Select Chat Service",
    ("OpenAI", "AWS Bedrock")
)

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.radio(
    "Navigation",
    (
        "Chat with Assistant",
        "Basic LLM Capabilities",
        "Agent-Based Alignment Generation",
        "Agent-Based Reasoning Systems",
    ),
)

def chat_llm(user_input):
    try:
        if chat_service == "OpenAI":
            endpoint = f"{BACKEND_URL}/chatopenai/"
            payload = {"model": "gpt-4o", "prompt": user_input}
        else:  # AWS Bedrock
            endpoint = f"{BACKEND_URL}/chatbedrock/"
            payload = {"model": "gpt-4o", "prompt": user_input} #todo bedrock model

        response = requests.post(endpoint, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        chat_response = response.json()  # Assume the API returns a JSON response

        assistant_message = chat_response.get("response", "")

        return assistant_message
    except Exception as e:
        st.error("Failed to get a response from the chat endpoint: " + str(e))


def main():
    # Initialize conversation history in session state
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # --------------------------- CHAT PAGE  --------------------------- #
    if option == "Chat with Assistant":
        st.title("Chat with Assistant")
        st.markdown("---")
        st.markdown(f"### Conversation History")

        # Display chat messages from history on app rerun
        for message in st.session_state.conversation_history:
            with st.chat_message(message["role"]):
                st.markdown(message["message"])


        # if user_input:
        if user_input := st.chat_input("Type your message here:"):
            st.session_state.conversation_history.append({"role": "user", "message": user_input})

            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                # response = st.write_stream(chat_llm(user_input)) # todo streaming
                response = st.write(chat_llm(user_input))

            assistant_message = chat_llm(user_input)
            st.session_state.conversation_history.append({"role": "assistant", "message": assistant_message})



    # --------------------------- BASIC LLM CAP PAGE  --------------------------- #
    elif option == "Basic LLM Capabilities":
        # Page Title
        st.title("Basic LLM Capabilities")

        # Example layout for Basic LLM Capabilities
        st.subheader("Grammar and Vocabulary Practice")
        st.write("Explore grammar, vocabulary, and reading comprehension tasks.")

        st.markdown("**Sample Grammar Exercise**")
        grammar_question = st.text_input("Enter a German sentence to analyze:")
        if st.button("Analyze Sentence"):
            st.write(f"Analyzing grammar for: {grammar_question}")
            # Placeholder analysis result
            st.info("Grammar analysis results go here.")

    elif option == "Agent-Based Alignment Generation":
        # Page Title
        st.title("Agent-Based Alignment Generation")

        # Example layout for Agent-Based Alignment
        st.subheader("Explore Model Alignment")
        st.write("Show how the model aligns with complex tasks or constraints.")

        st.markdown("**Alignment Demonstration**")
        scenario = st.text_area("Enter a scenario to test model alignment:")
        if st.button("Check Alignment"):
            st.write(f"Scenario: {scenario}")
            # Placeholder alignment results
            st.success("Alignment results go here.")

    elif option == "Agent-Based Reasoning Systems":
        # Page Title
        st.title("Agent-Based Reasoning Systems")

        # Example layout for Reasoning Systems
        st.subheader("Multi-step Reasoning and Chain-of-Thought")
        st.write("Demonstrate or test advanced reasoning capabilities.")

        st.markdown("**Reasoning Example**")
        reasoning_prompt = st.text_area("Enter a complex problem to solve:")
        if st.button("Run Reasoning"):
            st.write(f"Problem: {reasoning_prompt}")
            # Placeholder reasoning output
            st.warning("Reasoning steps or final answer go here.")

if __name__ == "__main__":
    main()
