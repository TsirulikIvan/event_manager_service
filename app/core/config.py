from pydantic import BaseConfig


class Setting(BaseConfig):
    DEFAULT_HOST: str = "localhost"
    DEFAULT_PORT: int = 8001
    SERVICE_NAME: str = "Event manager"
    DEBUG: bool = True


    class Config:
        env_file = ".env"
        case_sensitive = True