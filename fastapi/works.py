from datetime import datetime, timezone
from decimal import Decimal
from symtable import Class

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, Annotated
import re

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

class Post(BaseModel):
    author_id : Annotated[int, Field(..., gt=0, description="Идентификатор автора")]
    title : Annotated[str, Field(..., max_length=100, description="Заголовок записи, не более 100 символов")]
    description : Annotated[Optional[str], Field(default=None, max_length=100, description= "Описание записи, не более 250 символов")] = None
    content : Annotated[str, Field(description="Контент записи")]
    created_at : Annotated[Optional[datetime], Field(default_factory=lambda: datetime.now(timezone.utc), description="Запись создана")] = None
    updated_at : Annotated[Optional[datetime], Field(default=None, description="Запись обновлена")] = None
    is_published : Annotated[Optional[bool], Field(default= False, description="Запись опубликована")] = None
    tags : Annotated[Optional[list[str]], Field(default=[], description="Теги записи")] = None