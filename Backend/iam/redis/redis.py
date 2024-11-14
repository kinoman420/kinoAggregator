from redis import Redis
from loguru import logger

from db.Database.database import get_settings

config = get_settings()

try:
    redis_client = Redis(
        host=config.REDIS_URL,
        port=6379,
        charset="utf-8",
        decode_responses=True
    )
    

except Exception as e:
    redis_client = None


@logger.catch
def get_redis_client():
    return redis_client