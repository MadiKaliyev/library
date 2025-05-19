from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.crud.book import create_book, get_books, get_book, update_book, delete_book
from app.crud.api.deps import get_db, get_current_user

router = APIRouter()

@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.post("/", response_model=BookOut)
def create_new_book(book: BookCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_book(db, book)

@router.get("/{book_id}", response_model=BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return get_book(db, book_id)

@router.put("/{book_id}", response_model=BookOut)
def update_existing_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_book(db, book_id, book)

@router.delete("/{book_id}")
def delete_existing_book(book_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return delete_book(db, book_id)