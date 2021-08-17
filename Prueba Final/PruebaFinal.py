#API KEY NASA: PcSJslTQHn98bupJkZWlmdRRPKUIw2mz7gcNvtnp
import requests
import json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=PcSJslTQHn98bupJkZWlmdRRPKUIw2mz7gcNvtnp"


payload = {}
headers = {}
response = requests.request("GET", url,headers=headers, data=payload)
response = json.loads(response.text)

listaFotos = response["latest_photos"]

for i in listaFotos:
    listaFotos[i]
    print(listaFotos)