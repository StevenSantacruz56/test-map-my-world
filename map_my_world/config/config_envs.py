import os
from .db_envs import envs_postgres
from pydantic_settings import BaseSettings
from pydantic import BaseModel
import dotenv


def get_envs():
    if os.environ.get('DD_ENV', 'localhost') == 'localhost':
        dotenv.load_dotenv('envs/localhost.env')
        return os.environ


class Settings(BaseModel):
    DD_ENV: str = os.environ.get('DD_ENV', 'localhost')
    envs: object = get_envs()

    # PostgreSQL
    POSTGRES_URL: str = envs_postgres()
    POSTGRES_DEGUG: bool = envs.get('POSTGRES_DEGUG', False)

    @property
    def sync_database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_URL}"

    @property
    def async_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_URL}"


class ConfigEnv(BaseSettings):
    more_settings: Settings = Settings()
