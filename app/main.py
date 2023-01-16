from fastapi import FastAPI
import uvicorn

import db_methods, models, schemas
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


"""This method receives a json file with 3 fields: login, email and phone number.
   Then it checks the validity of the data using pydantic, and if the data is entered correctly,
   it adds a row with the data to the database"""
@app.post("/check")
async def check(user: schemas.User):
    new_user = db_methods.add_user(user)
    return {'id': new_user.id}


"""This method receives the user id as a number and returns that user's data"""
@app.get("/users/{user_id}")
async def users(user_id: int):
    user = db_methods.get_user_by_id(user_id)
    if user is None:
        return None
    return {'id': user.id, 'login': user.login, 'email': user.email, 'phone': user.phone}


if __name__ == "mane":
    uvicorn.run("main:app", host="localhost", port=30)
    print("YOU NEED TO GO -> http://localhost:30/")
