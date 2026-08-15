from sqlalchemy import Column, Integer, ForeignKey, Time, Boolean
from app.core.database import Base

class CafeHours(Base):
    __tablename__ = "cafe_hours"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafes.id"), nullable=False)
    day_of_week = Column(Integer, nullable=False)  # 0=Monday ... 6=Sunday
    opening_time = Column(Time, nullable=True)
    closing_time = Column(Time, nullable=True)
    is_closed = Column(Boolean, default=False)