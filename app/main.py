from fastapi import FastAPI
from app.api import hello

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/hello")
def hello_api(name: str):
    return hello(name)

# app/main.py에 슬쩍 추가해 보세요
#def bad_logic(data):
#        unused_var = 123  # Ruff가 잡아낼 것임
#    return eval(data) # Bandit/Semgrep이 잡아내고, CodeGemma가 수정을 제안할 것입니다.



