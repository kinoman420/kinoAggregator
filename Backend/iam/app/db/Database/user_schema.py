from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr

from .token_schema import TokenSchema


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str = Field(..., pattern=r".+@.+\.com")


class UserCreateSchema(UserBaseSchema):
    password: str

class AdminCreateSchema(UserCreateSchema):
    admin: bool


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserSchema(UserBaseSchema):
    id: UUID
    is_verified: bool

    class Config:
        from_attributes = True


class VerifyOTPSchema(BaseModel):
    email: str
    OTP: str


class ResendOTPSchema(BaseModel):
    email: str


class ResendOTPResponseSchema(BaseModel):
    email: str
    OTP: str
    message: str


class VerifyOTPResponseSchema(BaseModel):
    verified: bool
    message: str


class UserCreateResponseSchema(BaseModel):
    user: UserSchema
    OTP: str
    message: str


class UserLoginResponseSchema(BaseModel):
    user: UserSchema
    access_token: TokenSchema