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
    age: Optional[int] = None
    github: Optional[str] = None 

@app.get("/")
def read_root():
    return {"message": "My first fastapi build"} # dictionary

@app.get("/users/{user_id}")
def get_user(user_id:int = Path(..., description="the id you want to get", gt=-1, lt=100)):
    if user_id not in users:
        return HTTPException(status_code=204, detail="User Not Found")
    return users[user_id]

@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def post_user(user_id:int, user:User):
    if user_id not in users:
        raise HTTPException(status_code="400", detail="user already exist")
    users[user_id] = user.dict()
    return user

@app.put("/users/{user_id}")
def update_user(user_id:int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code="400", detail="User is not here")

    current_user = users[user_id] # the current user
    if user.name is not None:
        current_user["name"] = user.name
    if user.surname is not None:
        current_user["surname"] = user.surname
    if user.age is not None:
        current_user["age"] = user.age
    if user.github is not None:
        current_user["github"] = user.github
    return current_user

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code="400", detail="User is not here")
    deleted_user = users.pop(user_id)
    return {"message":"user has ben deleted", "deleted_user":deleted_user}

@app.get("/users/search/")
def search_by_name(name:str):
    if not name:
        return {"message":"Name parameter is required"}
    for user in users.values():
        if user["name"] == name:
            return user
    
    raise HTTPException(status_code="400", detail="User is not here")