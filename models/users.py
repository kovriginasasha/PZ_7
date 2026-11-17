
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    events: List[Event] = []


class NewUser(User):
    password: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
