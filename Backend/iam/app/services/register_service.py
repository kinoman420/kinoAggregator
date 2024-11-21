from typing import Annotated

from fastapi import Depends, HTTPException, status

from ..db.Database.user_schema import (
    UserCreateSchema,
    AdminCreateSchema,
    UserSchema,
    UserCreateResponseSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema,
    ResendOTPSchema,
    ResendOTPResponseSchema,
)
from ..services.auth.auth_service import AuthService
from ..services.auth.otp_service import OTPService
from .base_service import BaseService
from .user_service import UserService


class RegisterService(BaseService):
    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        auth_service: Annotated[AuthService, Depends()],
    ) -> None:
        super().__init__()

        self.user_service = user_service
        self.otp_service = otp_service
        self.auth_service = auth_service

    async def register_user(self, user: UserCreateSchema) -> UserCreateResponseSchema:
        existing_email = await self.user_service.get_user_by_email(
            user.email
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )

        new_user = await self.user_service.create_user(user)
        otp = self.otp_service.send_otp(new_user.email)

        return UserCreateResponseSchema(
            user=UserSchema.model_validate(new_user),
            OTP=otp,
            message="User created successfully, OTP sent to email",
        )
    

    async def register_admin(self, user: AdminCreateSchema) -> UserCreateResponseSchema:
        existing_email = await self.user_service.get_user_by_email(
            user.email
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Admin already exists"
            )

        new_user = await self.user_service.create_admin(user)
        otp = self.otp_service.send_otp(new_user.email)

        return UserCreateResponseSchema(
            user=UserSchema.model_validate(new_user),
            OTP=otp,
            message="Admin created successfully, OTP sent to email",
        )


    async def verify_user(
        self, verify_user_schema: VerifyOTPSchema
    ) -> VerifyOTPResponseSchema:
        if not self.otp_service.verify_otp(
            verify_user_schema.email, verify_user_schema.OTP
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP"
            )

        user = await self.user_service.get_user_by_email(
            verify_user_schema.email
        )

        await self.user_service.update_user(user.id, {"is_verified": True})

        return VerifyOTPResponseSchema(
            verified=True, message="User verified successfully"
        )

    async def resend_otp(
        self, resend_otp_schema: ResendOTPSchema
    ) -> ResendOTPResponseSchema:
        existing_user = await self.user_service.get_user_by_email(
            resend_otp_schema.email
        )
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )

        if existing_user.is_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already verified"
            )

        if self.otp_service.check_exist(resend_otp_schema.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="OTP already exists"
            )

        otp = self.otp_service.send_otp(resend_otp_schema.email)

        return ResendOTPResponseSchema(
            email=resend_otp_schema.email,
            OTP=otp,
            message="OTP sent to email",
        )