from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = "" # to generate key, use the command : ssl rand -hex 32
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

settings = Settings()
