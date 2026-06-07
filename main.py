from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

books: list[dict] = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear"
    },
    {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport"
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin"
    }
]

@app.get("/", include_in_schema=False) # doesnot show in api docs
async def root():
    return {"message": "Hello World"}

@app.get("/api/books")
async def get_books():
    return books

@app.get("/api/html", response_class=HTMLResponse)
async def html():
    return f"<h1>Hello This is HTML</h1>"
