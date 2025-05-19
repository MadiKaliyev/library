from sqlalchemy.orm import Session
from app.models.reader import Reader
from app.schemas.reader import ReaderCreate, ReaderUpdate
from fastapi import HTTPException


def get_readers(db: Session):
    return db.query(Reader).all()

def get_reader(db: Session, reader_id: int):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader

def create_reader(db: Session, reader: ReaderCreate):
    db_reader = Reader(**reader.dict())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader

def update_reader(db: Session, reader_id: int, reader_update: ReaderUpdate):
    reader = get_reader(db, reader_id)
    for field, value in reader_update.dict(exclude_unset=True).items():
        setattr(reader, field, value)
    db.commit()
    db.refresh(reader)
    return reader

def delete_reader(db: Session, reader_id: int):
    reader = get_reader(db, reader_id)
    db.delete(reader)
    db.commit()
    return {"ok": True}