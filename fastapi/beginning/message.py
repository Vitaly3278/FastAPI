from fastapi import FastAPI, status ,HTTPException
from pydantic import BaseModel

app = FastAPI()

class MessageCreate(BaseModel):
    content: str

class Message(BaseModel):
    id: int
    content: str

messages_db : list[Message] = [Message(id = 0, content="First post in FastAPI")]

@app.get("/messages", response_model=list[Message])
async def read_messages() -> list[Message]:
    return messages_db

@app.get("/messages/{message_id}", response_model=Message)
async def read_message(message_id: int) -> Message:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

@app.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(message_create: MessageCreate) -> Message:
    # Генерируем новый ID на основе максимального существующего
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=message_create.content)
    messages_db.append(new_message)
    return new_message

@app.put("/messages/{message_id}", response_model=Message)
async def update_message(message_id: int, message_create: MessageCreate) -> Message:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            updated_message = Message(id=message_id, content=message_create.content)
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
