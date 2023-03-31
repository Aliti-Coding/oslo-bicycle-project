from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Sequence, Float, delete
from sqlalchemy.orm import declarative_base, Session, sessionmaker
import json


def connect_2_db():
    with open(r"secret_folder\db_password.key", "r") as f:
        password_key = f.read()

    USERNAME = "fehmmialiti"
    PASSWORD = password_key
    PORT = 5432
    DATABASE = "oslo_sykkel_project"
    HOST = "bicycle-db.postgres.database.azure.com"


    Base = declarative_base() #mapper 
    engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    Base.metadata.bind = engine
    return Session(bind=engine)

