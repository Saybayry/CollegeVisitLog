# app/models/item.py

import uuid
from sqlmodel import Field, Relationship, SQLModel
from app.models.user import User

# Базовые свойства для Item
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)

# Модель Item в базе данных
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="items")

# Схемы для создания и обновления Item
class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)

# Публичная схема для Item
class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID

class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int
