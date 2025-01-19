import os
import shutil
from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse

class FileStorage:
    

    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_file(self, file: UploadFile) -> str:
        file_path = os.path.join(self.storage_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path

    def list_files(self):
        return [f for f in os.listdir(self.storage_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

    def get_file(self, filename: str):
        file_path = os.path.join(self.storage_dir, filename)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        return FileResponse(file_path, media_type="image/png" if filename.endswith(".png") else "image/jpeg")
