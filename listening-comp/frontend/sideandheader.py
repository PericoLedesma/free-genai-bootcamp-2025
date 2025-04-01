import streamlit as st

def render_header():
    """Render the header section"""
    st.title(" German Learning Assistant")
    st.markdown("""
    Transform YouTube transcripts into interactive Japanese learning experiences.

    This tool demonstrates:
    - Base LLM Capabilities
    - RAG (Retrieval Augmented Generation)
    - Amazon Bedrock Integration
    - Agent-based Learning Systems
    """)
    st.divider()  # 👈 Draws a horizontal rule


def render_sidebar():
    """Render the sidebar with component selection"""
    with st.sidebar:
        st.header("Development Stages")

        # Main component selection
        selected_stage = st.radio(
            "Select Stage:",
            [
                "1. Chat with Assistant",
                "2. Raw Transcript",
                "3. Structured Data",
                "4. RAG Implementation",
                "5. Interactive Learning"
            ]
        )

        # Stage descriptions
        stage_info = {
            "1. Chat with Assistant": """
            **Current Focus:**
            - Basic German learning
            - Understanding LLM capabilities
            - Identifying limitations
            """,

            "2. Raw Transcript": """
            **Current Focus:**
            - YouTube transcript download
            - Raw text visualization
            - Initial data examination
            """,

            "3. Structured Data": """
            **Current Focus:**
            - Text cleaning
            - Dialogue extraction
            - Data structuring
            """,

            "4. RAG Implementation": """
            **Current Focus:**
            - Bedrock embeddings
            - Vector storage
            - Context retrieval
            """,

            "5. Interactive Learning": """
            **Current Focus:**
            - Scenario generation
            - Audio synthesis
            - Interactive practice
            """
        }

        st.markdown("---")
        st.markdown(stage_info[selected_stage])

        return selected_stage