from typing import Generator
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy_utils import database_exists, create_database
from loguru import logger

class Settings(BaseSettings):
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DEBUG_MODE: bool
    REDIS_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OTP_EXPIRE_TIME: int

@lru_cache
@logger.catch
def get_settings():
    return Settings()

config = get_settings()




DATABASE_URL = (
    f"{config.DATABASE_DIALECT}://"
    f"{config.DATABASE_USERNAME}:"
    f"{config.DATABASE_PASSWORD}@"
    f"{config.DATABASE_HOSTNAME}:"
    f"{config.DATABASE_PORT}/"
    f"{config.DATABASE_NAME}"
)


engine = create_engine(DATABASE_URL, echo=config.DEBUG_MODE, future=True)

EntityBase = declarative_base()


def init_db() -> bool:
    EntityBase.metadata.create_all(bind=engine)
    logger.info("Database Initialized")
    return True


try:
    if not database_exists(engine.url):
        logger.info("Creating Database")
        create_database(engine.url)
        logger.info("Database Created")
except Exception as e:
    logger.error(f"Error: {e}")

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
logger.info("Database Session Created")


def get_entitybase():
    return EntityBase


def get_db() -> Generator[Session, None, None]:
    db = session_local()
    try:
        yield db
    except SQLAlchemyError as ex:
        logger.error(f"Database error during session: {ex}")
        db.rollback()  
        raise  
    finally:
        db.close()