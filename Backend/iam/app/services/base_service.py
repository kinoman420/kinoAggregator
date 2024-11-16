from ..db.Database.database import get_settings, Settings


class BaseService:
    def __init__(self, config: Settings = get_settings()) -> None:
        self.config = config