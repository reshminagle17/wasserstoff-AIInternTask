import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request 
from backend.app.api import upload, theme_identification , query 

app = FastAPI()

# Corrected directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
templates_dir = os.path.join(current_dir, "templates")

# Corrected mounting of static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers
app.include_router(upload.router)
app.include_router(theme_identification.router)
app.include_router(query.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Jinja templates directory
templates = Jinja2Templates(directory=templates_dir)

# Homepage route
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
