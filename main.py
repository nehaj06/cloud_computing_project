from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running Successfully"}

@app.get("/hello")
def hello():
    return {"message": "Hello World"}