from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.borrow import BorrowRequest, ReturnRequest, BorrowedOut
from app.crud.borrowed import borrow_book, return_book, get_active_borrows_by_reader
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/borrow", response_model=BorrowedOut)
def borrow(req: BorrowRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return borrow_book(db, req.book_id, req.reader_id)

@router.post("/return", response_model=BorrowedOut)
def return_(req: ReturnRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return return_book(db, req.book_id, req.reader_id)

@router.get("/reader/{reader_id}", response_model=list[BorrowedOut])
def list_reader_borrows(reader_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_active_borrows_by_reader(db, reader_id)