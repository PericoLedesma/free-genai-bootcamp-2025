# Frontend Specification

## Business Goal:
Language Listening Comprehension App. There are practice listening comprehension examples for language learning tests on youtube.
Pull the youtube content, and use that to generate out similar style listening comprehension.

## Technical Requirements:
* Must implement in Streamlit, pandas (data visualization)

------------------------
## Pages

#### Home Page
Chat with the assistant

![01_chat.png](images%2F01_chat.png)

#### Raw Transcript Page
Raw transcript from youtube video

![02_Raw transcript.png](images%2F02_Raw%20transcript.png)

#### Structured Data Page
Structured data from the raw transcript

It will extract from the video transcript the following per speaking practice question:
- Introduction 
- Conversation
- Question
- Answer

It will do it with a GenAI agent
It will take the raw transcript and generate structured data from the previous step
The transcript is stored in the backend

If there is an image, we have to describe it so we can generate it after
Maybe we can give some possible answers to the questions

Cambiamos solo a las que tienen que ver con el dialogo, la imagen es jodido

![03_Structured data.png](images%2F03_Structured%20data.png)



#### RAG Implementation Page
RAG implementation

![04_RAG implementation.png](images%2F04_RAG%20implementation.png)

#### Interactive Features Page
Interactive features

![05_Interactive features.png](images%2F05_Interactive%20features.png)