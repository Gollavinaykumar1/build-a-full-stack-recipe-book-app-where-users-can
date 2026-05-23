# models.py — table prefix: build_a_full_stack_recipe_book_app_where
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Item(Base):
    __tablename__ = "build_a_full_stack_recipe_book_app_where_items"
    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, index=True)
    description = Column(String, nullable=True)
    status      = Column(String, default="available")
    author      = Column(String, nullable=True)
    isbn        = Column(String, nullable=True)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
