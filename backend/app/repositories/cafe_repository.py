from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.cafe import Cafe, NoiseLevel
from app.models.cafe_amenity import CafeAmenity
from app.models.amenity import Amenity

class CafeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 20,
        noise_level: Optional[NoiseLevel] = None,
        amenities: Optional[List[str]] = None,
    ):
        query = self.db.query(Cafe)

        if noise_level:
            query = query.filter(Cafe.noise_level == noise_level)

        if amenities:
            for amenity_name in amenities:
                query = query.filter(
                    Cafe.id.in_(
                        self.db.query(CafeAmenity.cafe_id)
                        .join(Amenity, Amenity.id == CafeAmenity.amenity_id)
                        .filter(Amenity.name == amenity_name)
                    )
                )

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, cafe_id: int):
        return self.db.query(Cafe).filter(Cafe.id == cafe_id).first()