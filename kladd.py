import json 


# data = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 35},
#     {'name': 'Charlie', 'age': 40},
# ]


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
       
    # print(transformed_data)


batch_size = 10

for i in range(0, len(transformed_data), batch_size):
    # print(i)
    print("new batch!\n")
    batch = transformed_data[i:i+batch_size]
    print(batch)
