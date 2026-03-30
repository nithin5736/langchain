from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking for  monitoring & observability
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

# Streamlit UI framework
st.title("Langchain Demo (LLAMA2)")
input_text = st.text_input("Search by...")

# llama2 LLM
llm = ChatOllama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

# Execution
# Install the open source model using Ollama locally
# streamlit run ollama_chatbot.py