from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all origins so your app can be called from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Example marks data for 100 students (replace with your real data)
marks_data = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88,
    "Eva": 92,
    # add all your student names and marks here
}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    result = []
    for n in name:
        mark = marks_data.get(n, None)
        result.append(mark if mark is not None else 0)  # 0 if name not found
    return {"marks": result}
