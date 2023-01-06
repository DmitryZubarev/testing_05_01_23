from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Dobry vecher"


@app.post("/check")
async def check():
    pass


# хз какой реквест
@app.post(f"/users/")
async def users(user_id):
    pass
