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

class User(BaseModel):
    name: str
    surname: str
    age: int
    github: Optional[str] = None


class UpdateUser(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[str] = None
    github: Optional[str] = None 

@app.get("/")
def read_root():
    return {"message": "My first fastapi build"} # dictionary

@app.get("/users/{user_id}")
def get_user(user_id:int = Path(..., description="the id you want to get", gt=0, lt=100)):
    if user_id not in users:
        return HTTPException(status_code=204, detail="User Not Found")
    return users[user_id]

@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def post_user(user_id:int, user:User):
    if user_id in users:
        raise HTTPException(status_code="400", detail="user already exist")
    users[user_id] = user.dict()
    return user