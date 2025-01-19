import shutil
import os
from fastapi.responses import FileResponse
from fastapi import UploadFile, HTTPException
from infrastructure.file_storage import FileStorage

class MediaService:
    
    STORAGE_DIR = "uploads"

    def __init__(self):
        self.storage = FileStorage(self.STORAGE_DIR)

    async def upload_file(self, file: UploadFile):
        
        file_path = self.storage.save_file(file)
        return {"filename": file.filename, "url": f"/media/{file.filename}"}

    def list_files(self):
        
        return {"images": self.storage.list_files()}

    def get_file(self, filename: str):
        
        return self.storage.get_file(filename)

    def get_background_music(self):
        
        return self.storage.get_file("background.mp3")
