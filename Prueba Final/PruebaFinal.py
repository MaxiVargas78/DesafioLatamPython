import requests
import json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=PcSJslTQHn98bupJkZWlmdRRPKUIw2mz7gcNvtnp"
payload = {}
headers = {}
response = requests.request("GET", url,headers=headers, data=payload)
response = json.loads(response.text)

listaFotos = response["latest_photos"]

# REQUERIMIENTO NUMERO UNO
UpdateFoto = []
for i in range(25):
    UpdateFoto.append(listaFotos[i])

# REQUERIMIENTO NUMERO DOS
UrlFotos = []
for j in UpdateFoto:
    UrlFotos.append(j["img_src"])

# REQUERIMIENTO NUMERO TRES
def build_web_page(UrlFotos):
    html = ""
    for k in UrlFotos:
        html += "<li><img src=\"{}\"></li>\n".format(k)

    with open("HTML_NASA.html", "w") as f:
        f.write(" <html> \n <head> \n </head> \n <body> \n <ul>")
        f.write(html)
        f.write(" </ul> \n </body> \n </head> \n </html>")

build_web_page(UrlFotos)