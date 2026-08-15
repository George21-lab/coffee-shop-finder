import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.core.database import SessionLocal
from app.models.cafe import Cafe

SAMPLE_CAFES = [
    {
        "name": "Java House - Thika Road Mall",
        "address": "Thika Road Mall, Thika Road",
        "latitude": -1.2192,
        "longitude": 36.8878,
    },
    {
        "name": "Artcaffe - Two Rivers",
        "address": "Two Rivers Mall, Limuru Road",
        "latitude": -1.2087,
        "longitude": 36.7856,
    },
    {
        "name": "Java House - Thika Town",
        "address": "Kenyatta Highway, Thika",
        "latitude": -1.0396,
        "longitude": 37.0900,
    },
    {
        "name": "Kahawa Coffee House",
        "address": "Garden City, Thika Road",
        "latitude": -1.2225,
        "longitude": 36.8905,
    },
    {
        "name": "Dormans Coffee - Westgate",
        "address": "Westgate Mall, Mwanzi Road",
        "latitude": -1.2578,
        "longitude": 36.8034,
    },
]

def seed():
    db = SessionLocal()
    added = 0

    for data in SAMPLE_CAFES:
        exists = db.query(Cafe).filter(Cafe.name == data["name"]).first()
        if exists:
            continue

        cafe = Cafe(
            name=data["name"],
            address=data["address"],
            latitude=data["latitude"],
            longitude=data["longitude"],
        )
        db.add(cafe)
        added += 1

    db.commit()
    db.close()
    print(f"Seeded {added} cafes.")

if __name__ == "__main__":
    seed()