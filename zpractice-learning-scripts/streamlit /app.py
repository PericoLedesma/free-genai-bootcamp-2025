import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Simple Streamlit Chat App",
    page_icon=":speech_balloon:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Title for the chat application
st.title("Simple Streamlit Chat App")

# Initialize session state variables:
# - messages: to store the chat messages
# - chat_count: to track the total number of messages exchanged
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chat_count' not in st.session_state:
    st.session_state.chat_count = 0


def send_message():
    # Check if user input is not empty
    if st.session_state.user_input:
        # Append user's message to the chat history and update chat count
        st.session_state.messages.append(("User", st.session_state.user_input))
        st.session_state.chat_count += 1

        # Create a simple bot response (for example, echoing the message)
        bot_response = f"Echo: {st.session_state.user_input}"
        st.session_state.messages.append(("Bot", bot_response))
        st.session_state.chat_count += 1

        # Clear the input field
        st.session_state.user_input = ""


def reset_chat():
    # Reset the chat history and message count
    st.session_state.messages = []
    st.session_state.chat_count = 0


def main():
    # Display a welcome message
    st.markdown("Welcome to the chat app! Start by typing a message below.")

    # Provide a button to reset the chat
    if st.button("Reset Chat"):
        reset_chat()

    # Display the total number of messages exchanged
    st.markdown(f"**Total Messages:** {st.session_state.chat_count}")

    # Create an input widget for user messages
    st.text_input("Type your message and press Enter:", key="user_input", on_change=send_message)

    # Display the chat history
    for sender, message in st.session_state.messages:
        if sender == "User":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Bot:** {message}")


if __name__ == "__main__":
    main()
