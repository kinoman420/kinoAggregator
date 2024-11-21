from typing import Annotated, Dict
from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import User


class UserRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, updated_user: Dict) -> User:
        user_query = self.db.query(User).filter(User.id == user_id)
        db_user = user_query.first()
        user_query.filter(User.id == user_id).update(
            updated_user, synchronize_session=False
        )
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
        self.db.flush()

    def get_user(self, user_id: UUID) -> User:
        return self.db.get(User, user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()