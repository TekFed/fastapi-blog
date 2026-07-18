from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "TekFed Baefong",
        "title": "Learning about APIs",
        "content": "It has been really fun and insightful",
        "date-posted": "July 18, 2026", 
    },
    {
        "id": 2,
        "author": "John Sifu",
        "title": "On the Basics of Programming",
        "content": "Never stop learning. You can take your time, but never quit.",
        "date-posted": "July 17, 2026", 
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
