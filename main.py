import os
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv() # to read variables from .env

# Create Groq client to store the connection with groq's AI to use it later
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

print("🤖 Hi! I'm Medibot, your medical information chatbot.") #display introduction
print("Type 'bye' or 'quit' to stop.\n")

while True:
    user_input = input("👤 You: ") # wait for user to type something
    if user_input.lower() in ["bye", "quit"]: # convert input to lower case
        print("🤖 Medibot: Goodbye! It was nice talking to you stay healthy.") 
        break
    response = client.chat.completions.create(   # generate AI model responses for text conversation
        model="openai/gpt-oss-20b", # selecting the brain of the chatbot to generate the answers
        messages=[{ "role": "system","content": """
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
                {"role": "user","content": user_input}]
                
    )

    answer = response.choices[0].message.content # used to extract the text of the model's reply 

    print("\n🤖 Medibot:", answer)
    print() # for new line after every reply