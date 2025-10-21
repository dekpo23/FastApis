from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Optional
import random
import uvicorn
import os

load_dotenv()

app = FastAPI()

class format_data(BaseModel):
    Name: str = Field(..., max_length=100, example = "David Ekpo")
    track: str = Field(..., example = "AI Engineering")
    age: int = Field(..., example = 25)
    comments: Optional[str] = Field(None, example = "This program has been insightful but more can still be done.")

data = [
    {"ID": 1, "Name": "David Ekpo", "track": "AI Engineering", "age": 25, "comments": "None"},
    {"ID": 2, "Name": "Dolapo Onifade", "track": "AI Developer", "age": 26, "comments": "Fuck you"}
]

def get_dic(id):
    for i, dic in enumerate(data):
        if dic["ID"] == id:
            return i


@app.get("/")
def get_posts():
    return data

@app.get("/{id}")
def get_spec_posts(id: int):
    target_data = data[get_dic(id)]
    return target_data

@app.post("/users")
def post(pay_load: format_data):
    id = random.randint(10, 1000)
    dic = pay_load.model_dump()
    dic["ID"] = id
    data.append(dic)
    return data

@app.put("/users/{id}")
def update_post(payload: format_data, id: int):
    spec_id = get_dic(id)
    data[spec_id] = payload.model_dump()
    data[spec_id]["ID"] = id
    return data


@app.patch("/users/{id}")
def update_spec_post(payload:dict, id: int):
    spec_id = get_dic(id)
    data[spec_id].update(payload)
    return data

@app.delete("/users/{id}")
def delete_post(id: int):
    spec_id = get_dic(id)
    data.remove(data[spec_id])
    return data

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))



