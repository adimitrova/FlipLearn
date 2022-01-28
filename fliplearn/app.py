from tempfile import TemporaryFile
import uvicorn
from .contracts import Login, Card
from jinja2 import Environment, FileSystemLoader
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI, APIRouter
from pathlib import Path


app = FastAPI(
    title="Flip Cards API", openapi_url="/openapi.json"
)
app.mount("/", StaticFiles(directory="fliplearn/templates", html=True), name="static")
api_router = APIRouter()
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.post("/login")
def login(request: Login):
    if request.username == "ani" and request.password == "1234":
        return {"message": "Success"}
    return {"message": "Authentication Failed"}


@app.get("/")
def home():
    return {"Cards": []}


@app.route("/")
def index(request: Request) -> dict:
    # Load current count
    with open("count.txt", "r") as iFile:
        count = int(iFile.read())

    # Increment the count
    count = 3
    count += 1

    # Overwrite the count
    with open("count.txt", "w") as oFile:
        oFile.write(str(count))

    # Render HTML with count variable
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "count": count},
    )


@app.post("/cards")
def create_cards(request: Card):
    return {'cards': request}


if __name__ == "__main__":
    # uvicorn.run("app:app")
    uvicorn.run("app:app", host="http://127.0.0.1", port=8000, log_level="debug")

"""
Tutorials i'm following + URLs of other stuff:
https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
https://dashboard.heroku.com/apps
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6-jinja-templates/
"""