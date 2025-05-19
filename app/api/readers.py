from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.reader import ReaderCreate, ReaderUpdate, ReaderOut
from app.crud.reader import create_reader, get_readers, get_reader, update_reader, delete_reader
from app.crud.api.deps import get_db, get_current_user

router = APIRouter()

@router.get("/", response_model=list[ReaderOut])
def list_readers(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_readers(db)

@router.post("/", response_model=ReaderOut)
def create_new_reader(reader: ReaderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_reader(db, reader)

@router.get("/{reader_id}", response_model=ReaderOut)
def read_reader(reader_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_reader(db, reader_id)

@router.put("/{reader_id}", response_model=ReaderOut)
def update_existing_reader(reader_id: int, reader: ReaderUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_reader(db, reader_id, reader)

@router.delete("/{reader_id}")
def delete_existing_reader(reader_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return delete_reader(db, reader_id)