from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes import media

app = FastAPI()

app.include_router(media.router, prefix="/media", tags=["Media"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def home():
    return {"message": "Media Service Running"}
