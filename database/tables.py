from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Sequence, Float, delete, ForeignKey
from sqlalchemy.orm import declarative_base, Session, sessionmaker, relationship
import json
from connectdb import connection2db

Base = declarative_base()
engine = connection2db()


#connect to db
session = Session(bind=engine)

class Station(Base):
    __tablename__ = "station"

    station_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    android = Column(String)
    ios = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    capacity = Column(Integer)

    def __repr__(self):
        return f"<Station(stationd_id={self.station_id}, name={self.name},\
            address={self.address}, android{self.android}, ios={self.ios}),\
            lat={self.lat}, lon={self.lon}, capacity={self.capacity}>"

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

#syntax for creating all tables written as classes (a blueprint)
Base.metadata.create_all(engine)





if __name__ == '__main__':
    print("my name is jeff")

## Populating the station table 

    #reading the data we intend to populate


#deleting rows that was testing 
# user = session.query(Station).filter_by(name="fehmmi").all()
# stmt = delete(Station).where(Station.name == 'fehmmi') 
# session.delete(user[0])
# session.commit()