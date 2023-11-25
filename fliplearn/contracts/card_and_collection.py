from .base_model import BaseModel


class Card(BaseModel):
    class CardSides:
        front_side: str
        back_side: str

    card_id: str
    user_id: str
    collection_id: str
    card_sides: CardSides
    tag: str = None


class Collection(BaseModel):
    collection_id: str
    collection_title: str
    user_id: str
