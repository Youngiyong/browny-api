from typing import Optional

from pydantic import BaseModel


class ImageCreate(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "filename": "20210921015584057373",
                "full_path": "members/20210921015584057373"
            }
        }


class ImageResponse(BaseModel):
    filename: str
    full_path: str

    class Config:
        schema_extra = {
            "example": {
                "filename": "20210921015584057373",
                "full_path": "members/20210921015584057373"
            }
        }

