from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample marks dataset
student_marks = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40,
    "Eva": 50
}

@app.get("/api")
def get_marks(name: List[str] = []):
    return {"marks": [student_marks.get(n, 0) for n in name]}
