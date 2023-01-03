from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool


app = FastAPI()


@app.get('/hello-world')
async def hello_world():
    return {'message': 'Hello World'}


@app.post('/items')
async def create(item: Item):
    return {"item": item}
