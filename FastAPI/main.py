from models import *
from db import *
from services import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/chat',response_model=ChatResponse)
def chat(req : ChatRequest):

    session_id,history=get_or_create_session(req.session_id)
    history.append({'role':'user','content': req.message})
    reply=generate_reply(history)
    history.append({'role':'assistant','content': reply})
    return ChatResponse(session_id=session_id,reply=reply)

from fastapi.responses import StreamingResponse

def stream_reply(messages):

    chat = model.start_chat(history=[
        {"role": m["role"], "parts": [m["content"]]}
        for m in messages[:-1]
    ])

    response = chat.send_message(messages[-1]["content"], stream=True)

    for chunk in response:
        if chunk.text:
            yield chunk.text


@app.post("/chat/stream")
def chat_stream(req: ChatRequest):

    _, history = get_or_create_session(req.session_id)

    history.append({"role": "user", "content": req.message})

    return StreamingResponse(stream_reply(history), media_type="text/plain")