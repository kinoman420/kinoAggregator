from fastapi import FastAPI

from app.endpoints import user


app = FastAPI()
app.include_router(user.user_router)


  
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}