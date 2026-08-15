from sqlalchemy import Column, Integer, ForeignKey, Enum
import enum
from app.core.database import Base

class AmenityStatus(str, enum.Enum):
    confirmed = "confirmed"
    reported = "reported"
    disputed = "disputed"

class CafeAmenity(Base):
    __tablename__ = "cafe_amenities"

    cafe_id = Column(Integer, ForeignKey("cafes.id"), primary_key=True)
    amenity_id = Column(Integer, ForeignKey("amenities.id"), primary_key=True)
    status = Column(Enum(AmenityStatus), default=AmenityStatus.confirmed)