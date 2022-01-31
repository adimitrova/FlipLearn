import uvicorn
from .contracts import Login, Card
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from pathlib import Path
# from .schemas import RecipeSearchResults, Recipe, RecipeCreate
from .cards_data import CARDS as cards1
from .cards_data2 import CARDS as cards2

app = FastAPI(
    title="Flip Cards API", openapi_url="/openapi.json"
)
# app.mount("/", StaticFiles(directory="fliplearn/templates", html=True), name="static")
api_router = APIRouter()
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.post("/login")
def login(request: Login):
    if request.username == "ani" and request.password == "1234":
        return {"message": "Success"}
    return {"message": "Authentication Failed"}


@app.route("/")
def index(request: Request) -> dict:
    # Render HTML with count variable
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "count": len(cards2), "cards": cards2},
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


@app.get("/cards/{user_id}/card/{card_id}/{side}")
async def get_card_side(request: Request, user_id: int, card_id: int, side: str = "back"):
    for card in cards1:
        if card.get('user_id') == user_id:
            user_cards = card.get('cards')

    card = user_cards[card_id - 1]['card']
    return TEMPLATES.TemplateResponse(
        "single_card.html",
        {"request": request, "userID": user_id, "card": card, "side": side, "card_id": card_id}
    )


if __name__ == "__main__":
    # uvicorn.run("app:app")
    uvicorn.run("app:app", host="http://127.0.0.1", port=8000, log_level="debug")

"""
Tutorials i'm following + URLs of other stuff:
https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
https://dashboard.heroku.com/apps
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6-jinja-templates/
https://medium.com/@mikaelagurney/add-dynamic-components-to-your-html-templates-using-form-s-flask-and-jinja-59b4169ec3e1
"""
