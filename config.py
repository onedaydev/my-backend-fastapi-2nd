from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "6c41293056b7f5ddee900496653b5b1d7c24d25197a0ae3883b99b25eca7e27d" # openssl rand -hex 32
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

settings = Settings()
