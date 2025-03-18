import streamlit as st
import requests  # Import the requests library

BACKEND_URL = "http://127.0.0.1:8080"  # URL of the backend server

# Page configuration
st.set_page_config(
    page_title="German Learning Assistant",
    layout="wide",
)

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.radio(
    "Navigation",
    (
        "Chat with Claude",
        "Basic LLM Capabilities",
        "Agent-Based Alignment Generation",
        "Agent-Based Reasoning Systems",
    ),
)

def main():
    # --- MAIN PAGE CONTENT ---
    if option == "Chat with Claude":
        # Page Title
        st.title("Chat with Claude")

        # Example layout for Chat with Claude
        st.subheader("Chat Interface")
        st.write("Here you could implement a chat interface with Claude.")
        user_input = st.text_input("Type your message here:")

        # When the user clicks the Send button, make the API call
        if st.button("Send"):
            st.write(f"You asked Claude: {user_input}")
            # Prepare the payload based on the curl command
            payload = {"model": "gpt-4o", "prompt": user_input}
            try:
                response = requests.post(f"{BACKEND_URL}/chatopenai/", json=payload)
                response.raise_for_status()  # Raise an error for bad responses
                chat_response = response.json()  # Assume the API returns a JSON response
                st.write("ChatGPT response:", chat_response)
            except Exception as e:
                st.error("Failed to get a response from the chat endpoint: " + str(e))

    elif option == "Basic LLM Capabilities":
        # Page Title
        st.title("Basic LLM Capabilities")

        # Example layout for Basic LLM Capabilities
        st.subheader("Grammar and Vocabulary Practice")
        st.write("Explore grammar, vocabulary, and reading comprehension tasks.")

        st.markdown("**Sample Grammar Exercise**")
        grammar_question = st.text_input("Enter a Japanese sentence to analyze:")
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
