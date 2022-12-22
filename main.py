#!/usr/bin/env python

from fastapi import FastAPI, Depends,Response
from pydantic import BaseModel
import uvicorn
import db
import os
from typing import List
import click

app = FastAPI()

class User(BaseModel):
    name: str
    id: str

class MyResponse(BaseModel):
    data: List[User]

@app.post("/user/{user}")
def _put(user:str):
    id = ""
    try:
        id = db.writing(user)
        message = f"/{user} has been created"
    except Exception as e:
        message = str(e)
    return MyResponse(data=[User(name=user,id=id)])


@app.get("/user/{user}")
def _get(user):
    results = []
    try:
        results = db.query(user)
        data = [User(name=v["name"],id=v["id"]) for v in results]
        message = "got results"
    except Exception as e:
        message = str(e)
    return MyResponse(data=data)

@app.get("/")
def _check():
    return "ok\n"

@click.command()
@click.option("--worker", "-w", default=1)
@click.option("--port", "-p", default="8080")
def _run(worker: int, port: int, reload: bool):
    port = os.environ.get("PORT", port)
    options = {
            'port': int(port),
            'host': '0.0.0.0',
            'workers': worker,
            'reload': True,
        }
    print(options)
    uvicorn.run("main:app", **options)

if __name__ == '__main__':
    _run()
