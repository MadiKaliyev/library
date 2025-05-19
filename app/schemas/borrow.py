from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BorrowRequest(BaseModel):
    book_id: int
    reader_id: int

class ReturnRequest(BaseModel):
    book_id: int
    reader_id: int

class BorrowedOut(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrow_date: datetime
    return_date: Optional[datetime] = None

    class Config:
        from_attributes = True