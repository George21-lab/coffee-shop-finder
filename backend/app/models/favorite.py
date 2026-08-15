from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    cafe_id = Column(Integer, ForeignKey("cafes.id"), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())