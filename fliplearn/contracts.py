from pydantic import BaseModel, HttpUrl
from typing import Optional
from typing import Sequence

class CardData(BaseModel):
    front: str
    back: str


class Card(BaseModel):
    collection: str
    stack: str
    category: str
    card: CardData


class Login(BaseModel):
    username: str
    password: str
    agree_to_terms: Optional[bool]


class CardsSearchResults(BaseModel):
    results: Sequence[Card]


class CardCreate(BaseModel):
    collection: str
    stack: str
    category: str
    card: CardData
    user_id: int