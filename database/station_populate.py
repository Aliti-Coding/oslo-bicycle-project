import json
from tables import Station
from connectdb import connection2db
from sqlalchemy.orm import Session
import requests

#calling api 
response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json").json()



#connecting to db
engine = connection2db()
session = Session(bind=engine)


def formating(json):
    """function transforming data in flat json format
    """
    transformed_data = []

    for element in json['data']['stations']:
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
    return transformed_data



def station_api():
    """Returns a set data structure with all the current stations
    from the api call
    """
    data_transformed = formating(response)
    station_check_list = [int(row['station_id']) for row in data_transformed]
    return station_check_list




# check if station exist in database 
current_station = set(station_api())
existing_station = session.query(Station.station_id).all()
existing_station = set([stations[0] for stations in existing_station])


# check if there are any new stations uploaded in the from the api call
# if yes, add it to the database
compare_current_existing = current_station.difference(existing_station)


if len(compare_current_existing) > 0:

    # this is logic not necessary, but is efficient for huge big data injection to the database 
    # inserting rows in batches. increased effiency and avoid overload on database
    BATCH_SIZE = 10 #here you can decide how large batches you want to populate the table
    with session as se:

        for i in range(0, len(compare_current_existing), BATCH_SIZE):
            # print(i)
            print("new batch!\n")
            batch = compare_current_existing[i:i+BATCH_SIZE]
            print(batch)
            se.bulk_insert_mappings(Station, batch)
            se.commit()
