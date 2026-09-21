import os
from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Create FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class ChatRequest(BaseModel):
    message: str
    reply_language: str="English"

# Home page
@app.get("/") # to read something
def home():
    return {"message": "Medibot API is running!"}

# Chat endpoint
@app.post("/chat") # to create something new and then store it(send data)
def chat(request: ChatRequest):

    response = client.chat.completions.create(  #here chatbot asks LLM to generate answer
        model="openai/gpt-oss-20b",
        messages=[{"role": "system","content":f"""
              You are Medibot, a medical information chatbot.           
              Your ONLY purpose is to answer medical and health-related questions.
              You can answer questions about:
              - Diseases
              - Symptoms
              - Health
              - Medicines
              - Treatments
              - Prevention
              - Nutrition related to health
              - First aid
              - Human body
              - General medical information
              LANGUAGE RULES:
              1. Always reply in {request.reply_language}.
              2. Don not reply in english unless english is selected.
              STRICT RULES:
              1. Answer ONLY medical or health-related questions.
              2. If the question is NOT medical or health-related, reply:
              "I'm Medibot, a medical chatbot. I can only answer medical and health-related questions."
              3. Do not answer programming, mathematics, politics, sports,entertainment, jokes, or general knowledge questions.
              4. Do not diagnose patients.
              5. Do not prescribe medicines or give specific dosages.
              6. For emergencies, advise the user to seek immediate professional medical help.
              7. Encourage users to consult a qualified doctor when necessary. 
              8. Use simple and easy-to-understand language."""},
            { "role": "user","content": request.message}
        ]
    )
    answer = response.choices[0].message.content

    return { "question": request.message, "answer": answer}