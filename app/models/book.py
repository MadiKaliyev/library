from sqlalchemy import Column, Integer, String
from app.database.session import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
    isbn = Column(String, unique=True, nullable=True)
    count = Column(Integer, default=1)
    description = Column(String, nullable=True)
