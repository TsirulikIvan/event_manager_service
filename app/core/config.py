from pydantic import BaseConfig


class Setting(BaseConfig):
    DEFAULT_HOST: str = "localhost"
    DEFAULT_PORT: int = 8001
    SERVICE_NAME: str = "Event manager"
    DATABASE_URL: str = "localhost:5432/postgres"
    DEBUG: bool = True


    class Config:
        env_file = ".env"
        case_sensitive = True