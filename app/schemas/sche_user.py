from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import UserRole


class UserBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class Login(BaseModel):
    username_id: str
    password: str


class Register(BaseModel):
    full_name: str
    user_name: str
    email: EmailStr
    password: str
    phone_number: str


class UserDTO(BaseModel):
    id: int
    full_name: str
    user_name: str
    email: EmailStr
    phone_number: str
    role_name: str
    role_description: str


class UserNormalDTO(BaseModel):
    id: int
    company_id: int
    full_name: str
    user_name: str
    email: EmailStr
    phone_number: str
    role_name: str
    role_description: str


class ChangePassword(BaseModel):
    email: str
    current_password: str
    new_password: str
    confirm_new_password: str


class UserCreateRequest(UserBase):
    full_name: Optional[str]
    password: str
    email: EmailStr
    is_active: bool = True
    role: UserRole


class UserRegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole


class UserUpdateMeRequest(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]


class UserUpdateRequest(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool] = True
    role: Optional[UserRole]
