from typing import Annotated, Dict
from uuid import UUID
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
        return self.user_repository.create_user(
            User(
                username = user_body.username,
                email=user_body.email,
                hashed_password=self.hash_service.hash_password(user_body.password),
            )
        )
    
    async def create_admin(self, user_body: AdminCreateSchema) -> User:
        return self.user_repository.create_user(
            User(
                username = user_body.username,
                email=user_body.email,
                hashed_password=self.hash_service.hash_password(user_body.password),
                admin=True,
            )
        )

    async def update_user(self, user_id: int, update_fields: Dict) -> User:
        return self.user_repository.update_user(user_id, update_fields)

    async def delete_user(self, user: User) -> None:
        return self.user_repository.delete_user(user)

    async def get_user(self, user_id: UUID) -> User:
        return self.user_repository.get_user(user_id)

    
    
    async def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)