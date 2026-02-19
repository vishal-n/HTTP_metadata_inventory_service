from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://mongo:27017"
    DB_NAME: str = "metadata_db"


settings = Settings()
