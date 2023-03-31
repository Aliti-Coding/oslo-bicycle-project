import requests 
import json
import os
import sys, zipfile
# response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json").json()
# print(response)

# with open("tilgjengelighet.json", "w") as fp:
#     json.dump(response, fp, indent=4)


# with open("12.json", "r") as fp:
#     data = json.load(fp)

#     print(data)

# with open("december2022.json", "w") as outfile:
#     json.dump(data,outfile, indent=4)



# for x in os.listdir(r"C:\python_projects\oslo-bicycle-project"):
#     if x.endswith(".txt"):
#         print(x)


# test = sys.path.append(r"C:\Users\fehmm\Downloads\zip-file-test")
# map = os.listdir(r"C:\python_projects\oslo-bicycle-project")
# print(map)

# with zipfile.ZipFile(r'C:\python_projects\oslo-bicycle-project\zip-file-test.zip', 'r') as zipobj:
#     ziplist = zipobj.namelist()
#     print(ziplist)

#     with open(ziplist[0], 'r') as fp:
#         data = fp.read()



with zipfile.ZipFile(r'C:\python_projects\zip-file-test', 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        with zip_ref.open(file_name, 'r') as file:
            data = file.read()
            print(data)


