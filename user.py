from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

users = {
    1 :{
        "name": "Sivuyise",
        "surname": "matwa",
        "age": 20,
        "github": "http://github.com/Sivuyise15"
    },
    2 :{
        "name": "Thabo",
        "surname": "Mokwena",
        "age": 20,
        "github": "http://github.com/Thabo"
    }

}

@app.get("/")
def read_root():
    return {"message": "My first fastapi build"} # dictionary

@app.get("/users/{user_id}")
def get_user(user_id:int = Path(..., description="the id you want to get", gt=0, lt=100)):
    if user_id not in users:
        return HTTPException(status_code=204, detail="User Not Found")
    return users[user_id]

@app.post("/users/{user_id}")
def post_user(user_id:int = Path):
    users[user_id] = {
        "name": "Ahlume",
        "surname": "Matwa",
        "age": 10,
        "github": "http://github.com/A"
    }
    return 