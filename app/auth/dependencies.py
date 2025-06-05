from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .auth import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload  # ou récupérer l'utilisateur depuis la DB avec payload["sub"]

# def get_current_active_user(current_user: dict = Depends(get_current_user)):
#     if not current_user.get("is_active", True):
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
#     return current_user  # ou récupérer l'utilisateur depuis la DB avec current_user["sub"]