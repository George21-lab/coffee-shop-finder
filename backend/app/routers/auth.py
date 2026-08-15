from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService
from app.dependencies.auth_service import get_auth_service
from app.schemas.auth import SignupRequest, LoginRequest, TokenResponse
from app.exceptions.auth import EmailAlreadyRegisteredError, InvalidCredentialsError

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=TokenResponse)
def signup(payload: SignupRequest, service: AuthService = Depends(get_auth_service)):
    try:
        user, token = service.signup(payload.name, payload.email, payload.password)
    except EmailAlreadyRegisteredError:
        raise HTTPException(status_code=400, detail="Email already registered")
    return TokenResponse(access_token=token)

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, service: AuthService = Depends(get_auth_service)):
    try:
        user, token = service.login(payload.email, payload.password)
    except InvalidCredentialsError:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return TokenResponse(access_token=token)