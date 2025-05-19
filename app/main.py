from fastapi import FastAPI
from app.api import auth, books, readers, borrowed

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(readers.router, prefix="/readers", tags=["Readers"])
app.include_router(borrowed.router, prefix="/borrowed", tags=["Borrowed"])
