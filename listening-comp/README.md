# Listening Learning App
A progressive learning tool that demonstrates how RAG and agents can enhance language learning by grounding responses in real german lesson content. 
The system shows the evolution from basic LLM responses to a fully contextual learning assistant, helping students understand both the technical implementation and practical benefits of RAG.

### Business Goal: 
You are an Applied AI Engineer and you have been tasked to build a Language Listening Comprehension App. There are practice listening comprehension examples for language learning tests on youtube.
Pull the youtube content, and use that to generate out similar style listening comprehension.



## Technical Requirements:
- (Optional) Speech to Text, (ASR) Transcribe. eg Amazon Transcribe. OpenWhisper
- Youtube Transcript API (Download Transcript from Youtube)
- LLM + Tool Use “Agent”
- Sqlite3 - Knowledge Base 
- Text to Speech (TTS) eg. Amazon Polly
- AI Coding Assistant eg. Amazon Developer Q, Windsurf, Cursor, Github Copilot
- Frontend eg. Streamlit.
- Guardrails

* Must use Amazon Bedrock for:
   * API (converse, guardrails, embeddings, agents) (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
     * Aamzon Nova Micro for text generation (https://aws.amazon.com/ai/generative-ai/nova)
   * Titan for embeddings
* Must use SQLite for vector storage
* Must handle YouTube transcripts as knowledge source (YouTubeTranscriptApi: https://pypi.org/project/youtube-transcript-api/)
* Must demonstrate clear progression through stages:
   * Base LLM
   * Raw transcript
   * Structured data
   * RAG implementation
   * Interactive features
* Must maintain clear separation between components for teaching purposes
* Must include proper error handling for german text processing
* Must provide clear visualization of RAG process


## How to run the frontend:
``sh
streamlit run app.py
``
## How to run the backend:
``sh
cd backend
python main.py
``

