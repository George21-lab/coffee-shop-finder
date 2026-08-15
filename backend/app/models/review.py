from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class ReviewStatus(str, enum.Enum):
    published = "published"
    flagged = "flagged"
    removed = "removed"

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafes.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)  # e.g. 1-5
    comment = Column(String, nullable=True)
    status = Column(Enum(ReviewStatus), default=ReviewStatus.published)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())