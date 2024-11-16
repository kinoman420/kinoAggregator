from fastapi_restful.guid_type import GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, String, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .database import get_entitybase

EntityBase = get_entitybase()


class User(EntityBase):
    __tablename__ = "users"

    id = Column(
        UUID,
        primary_key=True,
        index=True,
        unique=True,
        nullable=False,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    admin = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=False)
