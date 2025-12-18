from fastapi import FastAPI
from app.api import hello

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/hello")
def hello_api(name: str):
    return hello(name)
