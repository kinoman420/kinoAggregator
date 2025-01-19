from fastapi import APIRouter, UploadFile, File, HTTPException
from services.media_service import MediaService

router = APIRouter()

media_service = MediaService()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    return await media_service.upload_file(file)

@router.get("/images")
async def list_images():
    
    return media_service.list_files()

@router.get("/image/{filename}")
async def get_image(filename: str):
    
    return media_service.get_file(filename)


