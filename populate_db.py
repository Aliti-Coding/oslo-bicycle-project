from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Sequence, Float, delete
from sqlalchemy.orm import declarative_base, Session, sessionmaker
import json

with open("db_password.key", "r") as f:
    password_key = f.read()

USERNAME = "fehmmialiti"
PASSWORD = password_key
PORT = 5432
DATABASE = "oslo_sykkel_project"
HOST = "bicycle-db.postgres.database.azure.com"


Base = declarative_base() #mapper 
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
Base.metadata.bind = engine
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
    

#syntax for creating all tables written as classes
# Base.metadata.create_all(engine)


#reading the data we intend to populate
with open("stasjoner.json", "r") as f:
    data = json.load(f)

    transformed_data = []

    for element in data['data']['stations']:
        transformed_data.append(
            {"station_id": element['station_id'], 
             "name": element['name'],
             "address": element['address'],
             "android": element['rental_uris']['android'],
             "ios": element['rental_uris']['ios'],
             "lat": element['lat'],
             "lon": element['lon'],
             "capacity": element['capacity']
             })
       

#inserting rows in batches. increased effiency and avoid overload on database
BATCH_SIZE = 10 #here you can decide how large batches you want to populate the table
with session as se:

    for i in range(0, len(transformed_data), BATCH_SIZE):
        # print(i)
        print("new batch!\n")
        batch = transformed_data[i:i+BATCH_SIZE]
        print(batch)
        se.bulk_insert_mappings(Station, batch)
        se.commit()







#deleting rows that was testing 
# user = session.query(Station).filter_by(name="fehmmi").all()
# stmt = delete(Station).where(Station.name == 'fehmmi') 
# session.delete(user[0])
# session.commit()