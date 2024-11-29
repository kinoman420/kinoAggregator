from typing import Optional

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    is_admin: bool
    token_type: str



