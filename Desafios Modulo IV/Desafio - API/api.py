import requests
import json

url = "https://reqres.in/api/users"
url2 = "https://reqres.in/api/users/2"

#Se utiliza json.dumps dada la recomendación del profesor, el diccionario de respuesta en cada caso se verá completo sin el
# json.dumps, con este último, no refleja los parametros del payload dentro de la respuesta.
payload = {}
payload1=json.dumps({"name": "ignacio", "job":"Profesor"})
payload2=json.dumps({"name": "morpheus", "resident": "zion"})
headers = {}

users_data = requests.request("GET", url, headers=headers, data=payload)
print(users_data.text)
print(users_data)
print("\n")

created_user = requests.request("POST", url, headers=headers, data=payload1)
print(created_user.text)
print(created_user)
print("\n")

updated_user = requests.request("PUT", url2, headers=headers, data=payload2)
print(updated_user.text)
print(updated_user)
print("\n")

deletePepe = requests.request("DELETE", url2, headers=headers, data=payload)
print("DELETE")
print("Código: "+str(deletePepe))
print("\n")