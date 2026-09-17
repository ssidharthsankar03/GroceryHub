from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    first_name: str = Field(min_length=2, max_length=100)
    last_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone_number: str = Field(min_length=10, max_length=20)
    password: str = Field(min_length=8, max_length=128)
    
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"