from typing import Annotated, Dict
from uuid import UUID
from loguru import logger
from fastapi import Depends

from ..db.Database.models import User
from ..db.Database.user_schema import UserCreateSchema, AdminCreateSchema
from ..db.Database.database_actions import UserRepository
from ..services.auth.hash_service import HashService
from ..services.base_service import BaseService


class UserService(BaseService):
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hash_service: Annotated[HashService, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hash_service = hash_service

    async def create_user(self, user_body: UserCreateSchema) -> User:
        logger.info(f"Creating user with email {user_body.email}")
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                hashed_password=self.hash_service.hash_password(user_body.password),
            )
        )
    
    async def create_admin(self, user_body: AdminCreateSchema) -> User:
        logger.info(f"Creating an admin with email {user_body.email}")
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                hashed_password=self.hash_service.hash_password(user_body.password),
                admin=True,
            )
        )

    async def update_user(self, user_id: int, update_fields: Dict) -> User:
        logger.info(f"Updating user with id {user_id}")
        return self.user_repository.update_user(user_id, update_fields)

    async def delete_user(self, user: User) -> None:
        logger.info(f"Deleting user with id {user.id}")
        return self.user_repository.delete_user(user)

    async def get_user(self, user_id: UUID) -> User:
        logger.info(f"Fetching user with id {user_id}")
        return self.user_repository.get_user(user_id)

    
    
    async def get_user_by_email(self, email: str) -> User:
        logger.info(f"Fetching user with email {email}")
        return self.user_repository.get_user_by_mobile_number(email)