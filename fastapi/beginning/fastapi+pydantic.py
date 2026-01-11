from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserCreate(BaseModel):
    name : Annotated[str, Field(...)]
    age : Annotated[int, Field(..., ge=18)]

class User(BaseModel):
    id : Annotated[int, Field(...)]
    name : Annotated[str, Field(...)]
    age : Annotated[int, Field(..., ge=18)]

users = []

@app.post("/users", response_model=User)
async def create_user(user_create: UserCreate) -> User:
    next_id = next_id = len(users) + 1
    new_user = User(id=next_id, name=user_create.name, age=user_create.age)
    users.append(new_user)
    return new_user

@app.get("/tasks", response_model=list[User])
async def list_tasks() -> list[User]:
    return users
