from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Example marks dictionary
    marks_dict = {
        "Alice": 10,
        "Bob": 20,
        "Charlie": 15
    }
    results = [marks_dict.get(n, 0) for n in name]
    return {"marks": results}

