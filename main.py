from fastapi import FastAPI
from schemas import User
import re
from db import get_user, add_user, get_user_by_data
import json


app = FastAPI()


def validate(login: str, email: str, phone: str):
    res = True
    error = ""

    # login
    if 3 <= len(login) <= 20:
        for char in login:
            if not (97 <= ord(char) <= 122 or 48 <= ord(char) <= 57 or ord(char) == 46):
                res = False
                error += "Incorrect login. "
    else:
        error += "Incorrect login. "
        res = False

    # email
    result = re.split("@", email)
    if result[0] == '' or result[1] == '':
        result.remove('')
    if (not len(result) == 2) or result[0][0] == '.':
        error += "Incorrect email. "
        res = False

    # phone
    if len(phone) == 12 and phone[0:3] == "+79":
        for char in phone[3:]:
            if not (48 <= ord(char) <= 57):
                error += "Incorrect phone. "
                res = False
    else:
        error += "Incorrect phone start or len. "
        res = False

    return res, error


@app.get("/")
async def root():
    return "Dobry vecher"


@app.post("/check")
async def check(user: User):
    val, er = validate(user.login, user.email, user.phone)
    if val:
        add_user(user.login, user.email, user.phone)
        user_id = get_user_by_data(user.login, user.email, user.phone)
        return {'id': user_id}
    else:
        return er


@app.get("/users/{user_id}")
async def users(user_id: int):
    user = get_user(user_id)
    return user
