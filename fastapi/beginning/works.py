# from datetime import datetime, timezone
# from decimal import Decimal
# from symtable import Class

# from pydantic import BaseModel, EmailStr, Field, field_validator
# from typing import Optional, Annotated
# import re

# class User(BaseModel):
#     username: str = Field(..., min_length=3, max_length=50, description="Имя пользователя"),
#     email : EmailStr = Field(..., description="Электронная почта пользователя"),
#     is_active : Optional[bool] = Field(default=True, description="Статус активности пользователя")


# class Task(BaseModel):
#     title: Annotated[str, Field(..., min_length=1, max_length=100, description="Название задачи")]
#     description: Annotated[Optional[str], Field(default=None, max_length=500, description="Описание задачи")] = None
#     is_completed : Annotated[Optional[bool], Field(default=False ,description="Статус завершения задачи")] = False

# class Order(BaseModel):
#     order_id: Annotated[int, Field(..., gt=0, description="Уникальный идентификатор заказа")]
#     user_id : Annotated[int, Field(..., gt=0, description="Идентификатор пользователя, сделавшего заказ")]
#     total_amount: Annotated[Decimal, Field(..., ge = 0.0, description="Общая сумма заказа")]
#     create_at : Annotated[datetime, Field(..., description= "Дата и время создания заказа")]

# class Address(BaseModel):
#     user_id : Annotated[int, Field(..., gt=0, description="Идентификатор пользователя")]
#     city : Annotated[str, Field(..., min_length=2, max_length=100, description="Город")]
#     street : Annotated[str, Field(..., min_length=2, max_length=200, description="Улица")]
#     postal_code : Annotated[int, Field(..., ge=101000,le=999999, description="Почтовый индекс")]

# from decimal import Decimal
#
# from pydantic import BaseModel, EmailStr, Field, field_validator
# from typing import Optional, Annotated
# import re
#
#
# class Product(BaseModel):
#     product_slug: Annotated[
#         str,
#         Field(
#             ...,
#             min_length=3,
#             max_length=120,
#             pattern=r'^[a-zA-Z0-9_-]+$',
#             description="Слаг продукта"
#         )
#     ]
#     name: Annotated[str, Field(..., min_length=3, max_length=100, description="Название продукта")]
#     price: Annotated[Decimal, Field(..., gt=0, description="Цена продукта")]
#     stock: Annotated[int, Field(default=0, ge=0, description="Количество продукта на складе")] = 0

# class Post(BaseModel):
#     author_id : Annotated[int, Field(..., gt=0, description="Идентификатор автора")]
#     title : Annotated[str, Field(..., max_length=100, description="Заголовок записи, не более 100 символов")]
#     description : Annotated[Optional[str], Field(default=None, max_length=100, description= "Описание записи, не более 250 символов")] = None
#     content : Annotated[str, Field(description="Контент записи")]
#     created_at : Annotated[Optional[datetime], Field(default_factory=lambda: datetime.now(timezone.utc), description="Запись создана")] = None
#     updated_at : Annotated[Optional[datetime], Field(default=None, description="Запись обновлена")] = None
#     is_published : Annotated[Optional[bool], Field(default= False, description="Запись опубликована")] = None
#     tags : Annotated[Optional[list[str]], Field(default=[], description="Теги записи")] = None

from fastapi import FastAPI, HTTPException, status, Depends
from typing import Annotated
from pydantic import BaseModel, Field, EmailStr
# app = FastAPI()
#
# class User(BaseModel):
#     id: Annotated[int, Field(...)]
#     name: Annotated[str, Field(...)]
#     email: Annotated[EmailStr, Field(...)]
#
# users = [
#     User(id=1, name="Алексей", email="alexey@example.com"),
#     User(id=2, name="Мария", email="maria@example.com"),
#     User(id=3, name="Иван", email="ivan@example.com"),
#     User(id=4, name="Елена", email="elena@example.com"),
#     User(id=5, name="Дмитрий", email="dmitry@example.com")
# ]
#
# @app.get("/users/{user_id}", response_model=User)
# async def get_user(user_id: int) -> User:
#     for user in users:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found" )

# app = FastAPI()
#
# class UserUpdate(BaseModel):
#     name : Annotated[str, Field(...)]
#     age : Annotated[int, Field(..., ge = 0)]
#
# class User(UserUpdate):
#     id: Annotated[int, Field(...)]
#
# users = [
#     User(id=1, name="Алексей", age=25),
#     User(id=2, name="Мария", age=30),
#     User(id=3, name="Иван", age=22),
#     User(id=4, name="Елена", age=28),
#     User(id=5, name="Дмитрий", age=35)
# ]
#
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, user_update: UserUpdate):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             updated_user = User(id=user_id, name=user_update.name, age=user_update.age)
#             users[i] = updated_user
#             return updated_user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#
# @app.get(
#     "/users",
#     response_model=list[User],
#     summary="Получить всех пользователей",
#     description="Возвращает список всех пользователей в системе",
#     tags=["Пользователи"]
# )
# async def get_all_users() -> list[User]:
#     return users
#     ------------------------------------------------------
from fastapi import FastAPI, HTTPException, status, Depends
from typing import Annotated
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Note(BaseModel):
    id: Annotated[int, Field(...)]
    text: Annotated[str, Field(...)]

notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for i, note in enumerate(notes):
        if note.id == note_id:
            deleted_note = notes.pop(i)
            return deleted_note

    raise HTTPException(status_code=404, detail="Note not found")

@app.get("/notes", response_model=list[Note])
async def get_all_users() -> list[Note]:
    return notes

