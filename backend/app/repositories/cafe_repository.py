from sqlalchemy.orm import Session
from app.models.cafe import Cafe

class CafeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 20):
        return self.db.query(Cafe).offset(skip).limit(limit).all()

    def get_by_id(self, cafe_id: int):
        return self.db.query(Cafe).filter(Cafe.id == cafe_id).first()