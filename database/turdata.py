import json
import sys, zipfile
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import create_engine, Table, ForeignKey,MetaData, Table, Column, Integer, String, DateTime, Sequence, Float, delete
from connectdb import connection2db
from database.tables import Station

engine = connection2db()
Base = declarative_base()
Base.metadata.bind = engine
#connection to db 
session = Session(bind=engine)


class Turhistorikk(Base):
    __tablename__  = "turhistorikk"
    tur_id = Column(Integer,Sequence('tur_id_seq'), primary_key=True)
    started_at = Column(DateTime)
    ended_at =  Column(DateTime)
    duration = Column(Integer)
    start_station_id = Column(Integer, ForeignKey('station.station_id'))
    start_station_name = Column(String)
    start_station_description = Column(String)
    start_station_latitude = Column(Float)
    start_station_longitude = Column(Float)
    end_station_id = Column(Integer, ForeignKey('station.station_id'))
    end_station_name = Column(Integer)
    end_station_description = Column(String)
    end_station_latitude = Column(Float)
    end_station_longitude = Column(Float)
    start_station = relationship('Station', foreign_keys=[start_station_id])
    end_station = relationship('Station', foreign_keys=[end_station_id])

    # def __init__(self, started_at,ended_at,duration)

Base.metadata.create_all(engine)







#access the json files with travel data
# with zipfile.ZipFile(r'turhistorikk.zip', 'r') as zip_ref:
#     for file_name in zip_ref.namelist():
#         with zip_ref.open(file_name, 'r') as file:
#             data = file.read()
#             print(data)

