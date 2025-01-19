from pydantic import BaseModel

class MediaFile(BaseModel):
    filename: str
    url: str
