from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.work_with_data import get_core_body_parts, get_sub_body_parts, get_exercises

app = FastAPI()


# Mount the static files directory for serving CSS and other static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Mount the templates directory for using Jinja2 templates
templates = Jinja2Templates(directory="app/templates")



# home_page route
@app.get("/", response_class=HTMLResponse)
async def core_body_parts_page(request: Request):


    #logika za hvatanje podataka
    data = get_core_body_parts()

    return templates.TemplateResponse("core_parts.html",{"request": request, "data": data})



# subgroups_page route
@app.get("/{core_part}/sub-body-part", response_class=HTMLResponse)
async def sub_body_parts_page(request: Request, core_part: str):
    
    #logika za hvatanje podataka
    sub_body_parts = []
    data = get_sub_body_parts()
    for sub_part in data:
        if sub_part.core_body_part.name == core_part:
            sub_body_parts.append(sub_part)
            

    return templates.TemplateResponse("sub_parts.html",{"request": request, "data": sub_body_parts})


# exercises_page route
@app.get("/{sub_part}/exercises", response_class=HTMLResponse)
async def exercises_page(request: Request, sub_part:str):

    #logika za hvatanje podataka
    sub_part = sub_part
    exercises = []
    data = get_exercises()
    for exercise in data:
        if exercise.sub_body_part.name == sub_part:
            exercises.append(exercise)

    return templates.TemplateResponse("exercises.html",{"request": request,  "data": exercises, "sub_part": sub_part})