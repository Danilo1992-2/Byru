from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:shaman@localhost:3306/Contash"
    DEBUG: bool = False
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
