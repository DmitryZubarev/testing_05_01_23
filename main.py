from fastapi import FastAPI
from schemas import User
from db import get_user, add_user, get_user_by_data


app = FastAPI()


@app.get("/")
async def root():
    return "Dobry vecher"


@app.post("/check")
async def check(user: User):
    add_user(user.login, user.email, user.phone)
    user_id = get_user_by_data(user.login, user.email, user.phone)
    return {'id': user_id}


@app.get("/users/{user_id}")
async def users(user_id: int):
    user = get_user(user_id)
    return user
