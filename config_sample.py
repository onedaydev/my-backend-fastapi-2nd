from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = ""

settings = Settings()
