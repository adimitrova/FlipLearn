from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from fliplearn.contracts import Collection


class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email_address: str
    agree_to_terms: Optional[bool]
    registration_date: datetime
    collections: List[Collection]


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
