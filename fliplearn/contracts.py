from pydantic import BaseModel


class CardData(BaseModel):
    front: str
    back: str


class Card(BaseModel):
    category: str
    stack: str
    card: CardData


class Login(BaseModel):
    username: str
    password: str
    agree_to_terms: Optional[bool]
