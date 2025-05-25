from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.get("/api")
def read_api():
    return {"message": "Hello from FastAPI!"}
