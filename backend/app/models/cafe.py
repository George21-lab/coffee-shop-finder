from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class NoiseLevel(str, enum.Enum):
    quiet = "quiet"
    moderate = "moderate"
    loud = "loud"

class VerificationStatus(str, enum.Enum):
    unverified = "unverified"
    verified = "verified"
    pending = "pending"

class Cafe(Base):
    __tablename__ = "cafes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    phone = Column(String, nullable=True)
    website_url = Column(String, nullable=True)
    price_level = Column(Integer, nullable=True)  # e.g. 1-4 ($ to $$$$)
    noise_level = Column(Enum(NoiseLevel), nullable=True)
    average_rating = Column(Float, default=0.0)
    review_count = Column(Integer, default=0)
    verification_status = Column(Enum(VerificationStatus), default=VerificationStatus.unverified)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())