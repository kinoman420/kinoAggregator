from fastapi import FastAPI

from app.endpoints import user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(user.user_router)

origins = [ "http://localhost:3000" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


  
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}