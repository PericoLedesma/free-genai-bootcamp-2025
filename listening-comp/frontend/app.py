import streamlit as st
import requests
import json
import re

from sideandheader import *

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


def chat_llm(user_input):
    try:
        if chat_service == "OpenAI":
            endpoint = f"{BACKEND_URL}/chatopenai/"
            payload = {"model": "gpt-4o", "prompt": user_input}
        else:  # AWS Bedrock
            endpoint = f"{BACKEND_URL}/chatbedrock/"
            payload = {"model": "gpt-4o", "prompt": user_input}  # todo bedrock model

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
        video = response.json()  # Assume the API returns a JSON response
        return video["video_title"], video["video_id"], video["transcript"]
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




# --------------------------- MAIN FUNCTION --------------------------- #
def main():
    render_header()
    option = render_sidebar()

    # # Debug section at the bottom
    # with st.expander("Debug Information"):
    #     st.json({
    #         "selected_stage": option,
    #         "transcript_loaded": st.session_state.transcript is not None,
    #         "chat_messages": len(st.session_state.messages)
    #     })

    # Initialize sesion variables
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    if 'video' not in st.session_state:
        st.session_state.video = {}

    # --------------------------- CHAT PAGE  --------------------------- #
    if option == "1. Chat with Assistant":
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


    # ------------------------------------------------------ #
    elif option == "2. Raw Transcript":
        st.subheader("Raw transcript Processing")
        url = st.text_input("Youtube URL: (accept for default video)")

        if st.button("Accept"):
            st.session_state.video = {"url": url}
            if url:
                st.info(f"Video URL: {url}")
            else:
                st.info(f"Video URL: Default")

            st.session_state.video["title"], st.session_state.video["id"], st.session_state.video["transcript"] = get_transcript(url)

            text_stats = get_text_stats(st.session_state.video["transcript"])
            st.session_state.video["character_count"] = text_stats["character_count"]
            st.session_state.video["word_count"] = text_stats["word_count"]
            st.session_state.video["sentence_count"] = text_stats["sentence_count"]
            st.session_state.video["line_count"] = text_stats["line_count"]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Raw transcript")

            if 'transcript' not in st.session_state.video:
                st.info(f"Ingest a video URL to get the transcript.")
            else:
                st.write(st.session_state.video["transcript"])

        with col2:
            st.subheader("Transcript Stats")
            if 'transcript' not in st.session_state.video:
                st.info(f"Ingest a video URL to get the transcript.")
            else:
                st.write("character_count")
                st.subheader(st.session_state.video["character_count"])

                st.write("word_count")
                st.subheader(st.session_state.video["word_count"])

                st.write("sentence_count")
                st.subheader(st.session_state.video["sentence_count"])

                st.write("line_count")
                st.subheader(st.session_state.video["line_count"])


    # ------------------------------------------------------ #
    elif option == "3. Structured Data":
        if 'id' not in st.session_state.video:
            st.info(f"Transcript video first")
        else:
            if 'struc_transcript' not in st.session_state:
                st.info(f"Structuring transcript  ... video id {st.session_state.video['id']}")
                try:
                    response = requests.post(f"{BACKEND_URL}/structdata/",
                                             json={"id": st.session_state.video["id"]})

                    response.raise_for_status()  # Raise an error for bad responses
                    video = response.json()  # Assume the API returns a JSON response
                    st.session_state.struc_transcript = video["struct_transcript"]
                    st.success(f"Transcript structured")
                except Exception as e:
                    st.error("Failed to get a response from the transcript endpoint: " + str(e))

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Transcript")
                st.markdown(f':red[Video title:]: **{st.session_state.video["title"]}**')
                st.markdown(f':red[Transcript:]: {st.session_state.video["transcript"]}')
                st.markdown(f':red[Transcript:]: {st.session_state.video["transcript"]}')

            with col2:
                st.subheader("Structured")
                transcript_struc = json.loads(st.session_state.struc_transcript)

                if transcript_struc["einleitung"] and transcript_struc["einleitung"]!="":
                    st.markdown(f"Einleitug: **{transcript_struc['einleitung']}**")
                else:
                    st.markdown("No einleitung")
                st.markdown("---")

                chat = transcript_struc["gespraech"]
                for msg in chat:
                    with st.chat_message(msg["sprecher"]):
                        #st.markdown(f'{msg["nachricht"]}')
                        #st.markdown(f'{msg["sprecher"]}->{msg["nachricht"]}')
                        st.markdown(f':red[{msg["sprecher"]}]: {msg["nachricht"]}')

    # ------------------------------------------------------ #
    elif option == "4. RAG Implementation":
        # I am going to store the conversation in vectors
        # First lets print the number of vectors stored

        st.markdown("**RAG Example**")
        reasoning_prompt = st.text_area("Enter a topic or question related to the conversation:")
        if st.button("Search about a topic"):
            st.write(f"Problem: {reasoning_prompt}")
            # Placeholder reasoning output
            st.warning("Reasoning steps or final answer go here.")

    elif option == "5. Interactive Learning":
        # Page Title
        st.title("Interactive Learning")

        # Example layout for Interactive Learning
        st.subheader("Interactive Learning Environment")
        st.write("Create a dynamic learning experience for users.")

        st.markdown("**Interactive Learning**")
        learning_scenario = st.text_area("Enter a learning scenario:")
        if st.button("Generate Scenario"):
            st.write(f"Scenario: {learning_scenario}")
            # Placeholder interactive learning output
            st.error("Interactive learning environment goes here.")


if __name__ == "__main__":
    main()
