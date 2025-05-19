from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    count: int = 1
    description: Optional[str] = None 

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    isbn: Optional[str] = None
    count: Optional[int] = None
    description: Optional[str] = None  

class BookOut(BookCreate):
    id: int

    class Config:
        from_attributes = True 
