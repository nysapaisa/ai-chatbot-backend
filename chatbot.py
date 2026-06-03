import anthropic
from config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS

# initialize the anthropic client
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# stores the full conversation so the bot remembers context
history = []

def chat(user_message: str) -> str:
    # add user message to history before sending
    history.append({
        "role": "user",
        "content": user_message
    })

    # call claude api with full history for context
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system="You are a helpful assistant. Keep answers clear and to the point.",
        messages=history
    )

    # extract the text from response
    reply = response.content[0].text

    # save assistant reply to history too
    history.append({
        "role": "assistant",
        "content": reply
    })

    return reply


def reset_chat():
    # clears history to start a fresh conversation
    global history
    history = []
    return {"message": "chat history cleared"}


def get_history():
    return history