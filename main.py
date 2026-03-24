from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SumRequest(BaseModel):
    a: int
    b: int

@app.get("/")
def read_root():
    return {"res": "Hello world"}

@app.get("/square")
def get_square(n: int):
    return {"result": n * n}

@app.get("/is_even")
def check_even(n: int):
    return {"result": n % 2 == 0}

@app.post("/sum")
def calculate_sum(data: SumRequest):
    return {"result": data.a + data.b}