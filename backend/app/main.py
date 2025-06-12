# import os
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.requests import Request 
# from backend.app.api import upload, theme_identification , query 

# app = FastAPI()

# # Corrected directory path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# static_dir = os.path.join(current_dir, "static")
# templates_dir = os.path.join(current_dir, "templates")

# # Corrected mounting of static directory
# app.mount("/static", StaticFiles(directory=static_dir), name="static")

# # Include routers
# app.include_router(upload.router)
# app.include_router(theme_identification.router)
# app.include_router(query.router)

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Jinja templates directory
# templates = Jinja2Templates(directory=templates_dir)

# # Homepage route
# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from backend.app.api import upload, theme_identification, query

app = FastAPI(
    title="Document Research & Theme Identification Chatbot",
    description="Wasserstoff AI Internship Project: Upload documents, run OCR, query for answers, and identify common themes.",
    version="1.0"
)

# Resolve base directory
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
templates_dir = os.path.join(current_dir, "templates")
data_dir = os.path.join(current_dir, "data")

# Ensure required folders exist
os.makedirs(static_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Load Jinja templates
templates = Jinja2Templates(directory=templates_dir)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(upload.router)
app.include_router(theme_identification.router)
app.include_router(query.router)

# Root route (homepage)
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Healthcheck endpoint (optional but useful for deployment/testing)
@app.get("/ping")
def ping():
    return {"message": "pong"}
