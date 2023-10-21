from pydantic import BaseModel


class Card(BaseModel):
    class CardSides:
        front_side: str
        back_side: str

    card_id: str
    user_id: str
    collection_id: str
    card_sides: CardSides
    collection_title: str = None
    tag: str = None


class Collection(BaseModel):
    collection_id: str
    collection_title: str
    user_id: str
