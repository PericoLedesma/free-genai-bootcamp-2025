import streamlit as st
import requests
import re

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
        "Raw Transcript",
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

def get_transcript(url):
    try:
        response = requests.post(f"{BACKEND_URL}/transcript/", json={"url": url})
        response.raise_for_status()  # Raise an error for bad responses
        transcript = response.json()  # Assume the API returns a JSON response
        return transcript["transcript"]
    except Exception as e:
        st.error("Failed to get a response from the transcript endpoint: " + str(e))


def get_text_stats(text: str) -> dict:
    character_count = len(text)

    # Split the text into words using default whitespace splitting
    words = text.split()
    word_count = len(words)

    # Split the text into sentences using a regex pattern to account for common sentence terminators
    sentences = re.split(r'[.!?]+', text.strip())
    # Filter out any empty strings that may appear after splitting
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Count the number of lines in the text
    line_count = len(text.splitlines())

    return {
        "character_count": character_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "line_count": line_count
    }


def main():
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    if 'video' not in st.session_state:
        st.session_state.video = {}
        st.session_state.video["character_count"] = ""
        st.session_state.video["word_count"] = ""
        st.session_state.video["sentence_count"] = ""
        st.session_state.video["line_count"] = ""
        st.session_state.video["video_transcript"] = ""

    # --------------------------- CHAT PAGE  --------------------------- #
    if option == "Chat with Assistant":
        st.title("Chat with Assistant")
        st.markdown("---")
        st.markdown(f"### Conversation History")

        for message in st.session_state.conversation_history:
            with st.chat_message(message["role"]):
                st.markdown(message["message"])

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
    elif option == "Raw Transcript":
        st.title("German Learning Assistant")
        st.write("Transform Youtube transcripts into interactive German learning experiences.")
        st.write("This tools demostrates: \n"
                 "- Base LLM capabilities\n "
                 "- RAG capabilities\n "
                 "- Amazon Bedrock capabilities\n"
                 "- Agent-based learning systems")

        st.subheader("Raw transcript Processing")
        url = st.text_input("Youtube URL")

        if st.button("Accept"):
            st.session_state.video = {"url": url}
            st.info(f"Video URL: {url}")
            st.session_state.video = {"video_transcript": get_transcript(url)}
            text_stats = get_text_stats(st.session_state.video["video_transcript"])
            st.session_state.video["character_count"] = text_stats["character_count"]
            st.session_state.video["word_count"] = text_stats["word_count"]
            st.session_state.video["sentence_count"] = text_stats["sentence_count"]
            st.session_state.video["line_count"] = text_stats["line_count"]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Raw transcript")
            st.write(st.session_state.video["video_transcript"])
        with col2:
            st.subheader("Transcript Stats")

            st.write("character_count")
            st.subheader(st.session_state.video["character_count"])

            st.write("word_count")
            st.subheader(st.session_state.video["word_count"])

            st.write("sentence_count")
            st.subheader(st.session_state.video["sentence_count"])

            st.write("line_count")
            st.subheader(st.session_state.video["line_count"])



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
