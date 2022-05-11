from sys import prefix
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, show_error: bool = False):
    error_text = "Неправильный логин или пароль" if show_error else ""
    return templates.TemplateResponse(
        "login.html", 
        {"request": request, "error_text": error_text}
    )


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(
        "main.html", 
        {"request": request}
    )


@app.get("/prof", response_class=HTMLResponse)
async def prof_page(request: Request):
    return templates.TemplateResponse(
        "prof.html", 
        {"request": request}
    )
