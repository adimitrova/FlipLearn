from typing import Optional
from datetime import datetime
from .base_model import BaseModel


class User(BaseModel):
    user_id: str
    username: str
    password: str
    first_name: str
    last_name: str
    email_address: str
    agree_to_terms: Optional[bool]
    registration_date: datetime


class Login(BaseModel):
    username: str
    password: str


class RegistrationForm(BaseModel):
    username: str
    password: str
    email_address: str
    first_name: str
    last_name: str
    agree_to_terms: Optional[bool]
    registration_date: datetime
