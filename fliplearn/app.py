import uvicorn
from fastapi import FastAPI
from contracts import Login, Card

app = FastAPI()


@app.post("/login")
def login(request: Login):
    if request.username == "ani" and request.password == "1234":
        return {"message": "Success"}
    return {"message": "Authentication Failed"}


@app.get("/")
def home():
    return {"Cards": []}


@app.post("/cards")
def create_cards(request: Card):
    return {'cards': request}


if __name__ == "__main__":
    uvicorn.run("app:app")
