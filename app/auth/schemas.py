from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
# class TokenData(BaseModel):
#     email: str | None = None
#     username: str | None = None
#     sub: str | None = None  # Subject, often used for user ID or unique identifier
#     avatar: str | None = None  # Optional avatar URL or identifier