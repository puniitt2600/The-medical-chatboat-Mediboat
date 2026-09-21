# The-medical-chatbot-Medibot
MediBot is an AI-powered medical chatbot built with FastAPI, Groq LLM, HTML, CSS, and JavaScript. It provides medical information about diseases, symptoms, medicines, treatments, and prevention, with voice input, text-to-speech, and multilingual support

🩺 MediBot – Medical AI Chatbot
MediBot is an AI-powered medical chatbot designed to provide information related to health and healthcare. It can answer questions about diseases, symptoms, medicines, treatments, and prevention.

Features
💬 AI-powered medical conversations
🩺 Answers medical and health-related questions
🎤 Voice input using Speech Recognition
🔊 Text-to-Speech for voice responses
🌐 Language selection for responses
🚫 Designed to focus only on medical-related questions
🌐 Simple and user-friendly web interface
Technologies Used
Python – Backend programming
FastAPI – Creates the backend API
Groq API – Connects the chatbot to the LLM
HTML – Creates the webpage structure
CSS – Designs the user interface
JavaScript – Handles chatbot interaction and voice features
Web Speech API – Speech recognition and text-to-speech
python-dotenv – Loads the API key securely from .env
How It Works
The user enters a medical question or speaks using the microphone.
JavaScript sends the question to the FastAPI backend.
FastAPI sends the question to the Groq LLM.
The LLM generates a medical-related response.
The response is sent back to the webpage.
The answer is displayed and can also be spoken using text-to-speech.
How to Run MediBot
Follow these steps to run MediBot on your computer.

1.Download the Project Clone the GitHub repository:
git clone YOUR_GITHUB_REPOSITORY_URL
cd MediBot
2.Install python
```bash
python --version
3. Create virtual environment
```bash
python -m venv venv
activate it
```bash
venv\Scripts\activate
4. Install Required libraries
```bash
pip install -r requirements.txt
5. Add your API Key
``` env
GROQ_API_KEY=your_groq_api_key_here
6. Start the FAST API
```bash
uvicorn main:app --reload
7. Open your index.html in web browser using LIVE SERVER.
