import requests
import streamlit as st

def generate_gemini_response(input_text):
    response=requests.post("http://localhost:8080/essay/invoke",
    json = {'input': {'topic': input_text}})

    return response.json()['output']['content']

def generate_ollama_response(input_text):
    response=requests.post("http://localhost:8080/poem/invoke",
    json={'input': {'topic': input_text}})

    return response.json()['output']

# Streamlit UI
input_text1=st.text_input("Write essay on")
input_text2=st.text_input("Write poem on")

if input_text1:
    st.write(generate_gemini_response(input_text1))

if input_text2:
    st.write(generate_ollama_response(input_text2))

# Run cmds
# python3 -m streamlit run client.py