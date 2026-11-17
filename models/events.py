
from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://example.com/image.png",
                "description": "Presentation of a new book",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }
