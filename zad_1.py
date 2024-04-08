"""
Stworzyć endpoint, który zwraca respone {'hello': 'world'}, uruchomić serwer
i sprawdzić w przeglądarce czy endpoint zwraca odpowiednie dane.
"""

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/test")
async def root():
    return {"hello": "world"}
