from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.services.cafe_service import CafeService
from app.dependencies.cafe import get_cafe_service
from app.schemas.cafe import CafeOut
from app.models.cafe import NoiseLevel

router = APIRouter(prefix="/cafes", tags=["cafes"])

@router.get("/", response_model=List[CafeOut])
def list_cafes(
    skip: int = 0,
    limit: int = 20,
    noise_level: Optional[NoiseLevel] = None,
    amenities: Optional[List[str]] = Query(None),
    service: CafeService = Depends(get_cafe_service),
):
    return service.list_cafes(skip=skip, limit=limit, noise_level=noise_level, amenities=amenities)

@router.get("/{cafe_id}", response_model=CafeOut)
def get_cafe(cafe_id: int, service: CafeService = Depends(get_cafe_service)):
    cafe = service.get_cafe(cafe_id)
    if not cafe:
        raise HTTPException(status_code=404, detail="Cafe not found")
    return cafe