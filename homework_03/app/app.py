from fastapi import FastAPI, Body
from typing import List

from schemas import UserIn, UserOut
import crud

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!!!!"}


@app.get("/{user_id}/friends/")
def get_friends(user_id: int):
    return {
        "id": user_id,
        "friends": [
            {
                "id": 2342,
                "bd": None,
                "close_friend": False
            }
        ],
    }


@app.post("/content_id/")
def create_content_id(content_id: dict = Body(...)):
    return {
        "content_id": content_id,
    }


@app.post("/items/")
def create_item(data: dict = Body(...)):
    return {
        "item": data
    }


@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserIn):
    user = crud.create_user(user_in)
    return user


@app.get("/users/", response_model=List[UserOut])
def get_users():
    users = crud.list_users()
    return users


@app.get("/ping/")
def get_ping():
    return {"message": "pong"}
