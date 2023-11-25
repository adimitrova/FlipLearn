import uvicorn
import os

# from Fliplearn.fliplearn.contracts import Login, Card
from fliplearn.contracts import Login, Card
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Form
from pathlib import Path
# from .schemas import RecipeSearchResults, Recipe, RecipeCreate
from fliplearn.cards_data import CARDS as cards1
from fliplearn.cards_data2 import CARDS as cards2

app = FastAPI(
    title="Flip Cards API", openapi_url="/openapi.json"
)
api_router = APIRouter()
app_dir = os.path.dirname(__file__)     # abs path
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

# Mount the full path of static files
app.mount("/static",
          StaticFiles(directory=os.path.join(app_dir, "static/"), html=True),
          name="static")  # To load normal html files or images etc


@app.post("/login")
async def login(username: str = Form(...), password: str = Form):
    print(password)
    return {'username': username}


@app.route("/")
def index(request: Request) -> Jinja2Templates.TemplateResponse:
    # Render HTML with count variable
    # TODO: Should show all collections to the user and option to create a new collection
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request},
    )


@app.post("/cards")
def create_cards(request: Card):
    return {'cards': request}


@app.get("/cards/{user_id}")
def get_cards_for_user(request: Request, user_id: int):
    for card in cards1:
        if card.get('user_id') == user_id:
            user_cards = card.get('cards')

    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "userID": user_id, "count": len(user_cards), "cards": user_cards},
    )


@app.get("/collections/{user_id}")
def get_collections_for_user(request: Request, user_id: int) -> Jinja2Templates.TemplateResponse:
    for card in cards1:
        if card.get('user_id') == user_id:
            user_cards = card.get('cards')

    collections = set()
    for c in user_cards:
        collections.add(c['collection'])

    return TEMPLATES.TemplateResponse(
        "collections.html",
        {"request": request, "user_id": user_id, "collections": collections}
    )


@app.get("/collections/{user_id}/{collection_name}")
def get_collections_for_user(request: Request, user_id: int, collection_name: str) -> dict:
    # current_user_cards =  # query db here
    cards_in_collection = dict()
    for item in cards1:
        if item['user_id'] == user_id:
            cards = item['cards']

    for card in cards:
        if card['collection'].lower() == collection_name.lower():
            cards_in_collection.update(card)
    return cards_in_collection


@app.get("/cards/{user_id}/card/{card_id}/{side}")
async def get_card_side(request: Request, user_id: int, card_id: int,
                        side: str = "back") -> Jinja2Templates.TemplateResponse:
    for card in cards1:
        if card.get('user_id') == user_id:
            user_cards = card.get('cards')

    full_card_data = user_cards[card_id - 1]
    card = full_card_data['card']
    return TEMPLATES.TemplateResponse(
        "single_card.html",
        {"request": request, "user_id": user_id, "card": card, "side": side, "card_id": card_id,
         "tag": full_card_data.get('tag')}
    )


def run_app():
    uvicorn.run("app:app", reload=True)


if __name__ == "__main__":
    run_app()
