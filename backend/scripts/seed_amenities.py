import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.core.database import SessionLocal
from app.models.amenity import Amenity
from app.models.cafe_amenity import CafeAmenity
from app.models.cafe import Cafe

AMENITIES = [
    {"name": "wifi", "category": "connectivity"},
    {"name": "outlets", "category": "connectivity"},
    {"name": "outdoor_seating", "category": "seating"},
    {"name": "indoor_seating", "category": "seating"},
]

def seed():
    db = SessionLocal()

    amenity_objs = {}
    for a in AMENITIES:
        existing = db.query(Amenity).filter(Amenity.name == a["name"]).first()
        if not existing:
            existing = Amenity(name=a["name"], category=a["category"])
            db.add(existing)
            db.commit()
            db.refresh(existing)
        amenity_objs[a["name"]] = existing

    cafes = db.query(Cafe).limit(3).all()
    for cafe in cafes:
        for amenity_name in ["wifi", "outlets"]:
            amenity = amenity_objs[amenity_name]
            exists = db.query(CafeAmenity).filter(
                CafeAmenity.cafe_id == cafe.id,
                CafeAmenity.amenity_id == amenity.id
            ).first()
            if not exists:
                db.add(CafeAmenity(cafe_id=cafe.id, amenity_id=amenity.id))

    db.commit()
    db.close()
    print("Amenities seeded and linked.")

if __name__ == "__main__":
    seed()