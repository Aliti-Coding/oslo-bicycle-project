import json
import sys, zipfile
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine, Table, ForeignKey,MetaData, Table, Column, Integer, String, DateTime, Sequence, Float, delete
from connectdb import connection2db
from tables import Turhistorikk

engine = connection2db()
Base = declarative_base()

#connection to db 
session = Session(bind=engine)


#access the json files with travel data
with zipfile.ZipFile(r'turhistorikk.zip', 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        with zip_ref.open(file_name, 'r') as file:
            data = json.load(file)

            #convert station_id from string to integer
            for l in data:
                start_station = int(l['start_station_id'])
                l['start_station_id'] = start_station
                
                end_station = int(l['end_station_id'])
                l['end_station_id'] = end_station


BATCH_SIZE = 1000


with session as se:

    for row in range(0, len(data), BATCH_SIZE):
        batch = data[row:row+BATCH_SIZE]
        
        # try-except block i needed because historical data contains station_id that does not exist in station table
        # most likly those are stations removed from the station api
        # to solve this problem we just skip this batch that causes the error
        try:
            se.bulk_insert_mappings(Turhistorikk, batch)
            se.commit()
        except IntegrityError:
            se.rollback() #if error occurs we rollback the transaction to the database so we can ensure data consitency
            for rows in batch:
                print(f"Skipping trip with start_station_id = {rows['start_station_id']} or end_station_id = {rows['end_station_id']} because of error then, skip batch")
            continue