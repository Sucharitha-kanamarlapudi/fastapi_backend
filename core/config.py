import os
from dotenv import load_dotenv

from pathlib import Path
print(Path('.'))
env_path = Path('.')/'.env'
print(env_path)
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Blog"
    PROJECT_VERSION: str = "0.1.0"

    MYSQL_USER: str =os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str =os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str =os.getenv("MYSQL_SERVER")
    MYSQL_PORT: int =os.getenv("MYSQL_PORT")
    MYSQL_DB: str =os.getenv("MYSQL_DB")
    DATABASE_URL: str=f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
settings=Settings()
