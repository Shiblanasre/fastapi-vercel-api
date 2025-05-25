from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Sample hardcoded student marks (replace with file data if needed)
student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65
}

app = FastAPI()

# ✅ Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [student_marks.get(n, None) for n in name]
    return {"marks": result}
