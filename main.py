from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts
