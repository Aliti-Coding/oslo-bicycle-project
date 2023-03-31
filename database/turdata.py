import requests 
import json
import os
import sys, zipfile



with zipfile.ZipFile(r'turhistorikk.zip', 'r') as zip_ref:
    for file_name in zip_ref.namelist():
       
        with zip_ref.open(file_name, 'r') as file:
            data = file.read()
            print(data)


