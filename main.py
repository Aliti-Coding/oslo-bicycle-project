import requests 
import json

# response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json").json()
# print(response)

# with open("tilgjengelighet.json", "w") as fp:
#     json.dump(response, fp, indent=4)


with open("11.json", "r") as fp:
    data = json.load(fp)

    print(data)