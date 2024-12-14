import os
from dotenv import load_dotenv


load_dotenv("../.env")


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{db_host}:5432/{db_name}".format(
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        db_host=os.environ.get("POSTGRES_HOST"),
        db_name=os.environ.get("POSTGRES_DB")
    )
    SECRET_KEY = os.environ.get("SECRET_KEY")