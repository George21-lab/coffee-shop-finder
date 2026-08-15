from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.cafe_repository import CafeRepository
from app.services.cafe_service import CafeService

def get_cafe_service(db: Session = Depends(get_db)) -> CafeService:
    repository = CafeRepository(db)
    return CafeService(repository)