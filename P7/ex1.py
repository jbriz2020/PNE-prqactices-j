import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
#print(response)
answer_decoded = response.read().decode()
#print(type(answer_decoded), answer_decoded)
dict_response = json.loads(answer_decoded)  # to transform str to dict
#print(type(dict_response), dict_response)

print(f"Server: {SERVER}")
print(f"URL: {URL}")

if dict_response["ping"] == 1:
    print("PING OK!!! The database is running")
else:
    print("Database is down!!!")