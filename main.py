from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import chat, reset_chat, get_history

app = FastAPI(title="AI Chatbot Backend")

# allow frontend to connect to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# message format expected from user
class UserMessage(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "chatbot is running"}

# main chat endpoint
@app.post("/chat")
def send_message(body: UserMessage):
    reply = chat(body.message)
    return {"response": reply}

# get full conversation history
@app.get("/history")
def conversation_history():
    return {"history": get_history()}

# reset the conversation
@app.post("/reset")
def reset():
    return reset_chat()