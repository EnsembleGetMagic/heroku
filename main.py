import imp
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {f"message ":f"feb1 test working"}