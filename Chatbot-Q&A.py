import os

from dotenv import load_dotenv
load_dotenv()

import streamlit as st

#Import env variables
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
groq_api_key = os.getenv("GROQ_API_KEY")



# Streamlit sliders for user-controlled parameters
temperature = st.sidebar.slider("Select Temperature (creativity)", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
max_tokens = st.sidebar.slider("Select Max Tokens (response length)", min_value=50, max_value=1024, value=300, step=50)



#Import Langchain_groq LLM Model
from langchain_groq import ChatGroq
llm= ChatGroq(
   model="gemma2-9b-it",
   groq_api_key=groq_api_key,
   temperature=temperature,
   max_tokens=max_tokens)


#Create Chat-Prompt
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are assistant, please help the user to answer their questions"),
        ("human"," {input}")
    ]
)


# Build chain (using LCEL)-> as there is no retriever and document it is just LLM QA Chatbot 
chain = prompt | llm



def generate_response(question):
    answer= chain.invoke({"input":question})

    return answer



st.title("Q&A Chatbot With Gemma Model")

input_text=st.text_input("Go ahead and ask any question")

if input_text:

 response=generate_response(input_text)
 st.write(response.content)
 
else:
   st.write("Please write some query")