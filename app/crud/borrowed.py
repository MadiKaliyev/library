from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException
from app.models.borrowed import BorrowedBook
from app.models.book import Book
from app.models.reader import Reader


def borrow_book(db: Session, book_id: int, reader_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or book.count <= 0:
        raise HTTPException(status_code=400, detail="No available copies of the book")

    active_loans = db.query(BorrowedBook).filter(
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date.is_(None)
    ).count()

    if active_loans >= 3:
        raise HTTPException(status_code=400, detail="Reader already has 3 active books")

    borrowed = BorrowedBook(book_id=book_id, reader_id=reader_id)
    book.count -= 1
    db.add(borrowed)
    db.commit()
    db.refresh(borrowed)
    return borrowed


def return_book(db: Session, book_id: int, reader_id: int):
    record = db.query(BorrowedBook).filter(
        BorrowedBook.book_id == book_id,
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date.is_(None)
    ).first()

    if not record:
        raise HTTPException(status_code=400, detail="This book is not currently borrowed by this reader")

    record.return_date = datetime.utcnow()
    book = db.query(Book).filter(Book.id == book_id).first()
    book.count += 1
    db.commit()
    db.refresh(record)
    return record


def get_active_borrows_by_reader(db: Session, reader_id: int):
    return db.query(BorrowedBook).filter(
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date.is_(None)
    ).all()
