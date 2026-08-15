from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CafeOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    address: str
    latitude: float
    longitude: float
    phone: Optional[str] = None
    website_url: Optional[str] = None
    price_level: Optional[int] = None
    average_rating: float
    review_count: int
    created_at: datetime

    class Config:
        from_attributes = True