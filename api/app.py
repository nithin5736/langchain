from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

# Env Variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# FastAPI Application Context
app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API server"
)

# APIs with direct access to model
add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    path="/gemini"
)

# Models
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = Ollama(model="llama2")

# Prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# APIs with prompt and model chain
add_routes(
    app,
    prompt1| model1,
    path="/essay"
)

add_routes(
    app,
    prompt2|model2,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)


# Execution
# pyton3 app.py
# /docs -> swagger UI

