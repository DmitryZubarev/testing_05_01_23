from fastapi import FastAPI
from schemas import User
from db import get_user, add_user, get_user_by_data

app = FastAPI()


"""Root method say 'Hello' to our best users"""
@app.get("/")
async def root():
    return "Dobry vecher"


"""This method receives a json file with 3 fields: login, email and phone number.
   Then it checks the validity of the data using pydantic, and if the data is entered correctly,
   it adds a row with the data to the database"""
@app.post("/check")
async def check(user: User):
    add_user(user.login, user.email, user.phone)
    user_id = get_user_by_data(user.login, user.email, user.phone)
    return {'id': user_id}


"""This method receives the user id as a number and returns that user's data"""
@app.get("/users/{user_id}")
async def users(user_id: int):
    user = get_user(user_id)
    return user
