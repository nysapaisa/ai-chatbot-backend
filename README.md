# AI Chatbot Backend

A backend REST API built with FastAPI that integrates with 
Anthropic's Claude API to power an AI chatbot with 
conversation memory.

## Tech Stack
- Python, FastAPI, Anthropic Claude API

## Features
- Multi-turn conversation with memory
- REST API endpoints for chat, history, reset
- Modular service architecture
- Environment-based config for secure API key management

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /chat | Send a message |
| GET | /history | Get conversation history |
| POST | /reset | Reset conversation |