# Citation (IEEE FORMATTED)
# hallessandro, How to create a HTTP server with Python . Hallessandro D´villa  [webpage]
# https://hallessandro.github.io/programming/http_server_with_python.html 

# You need to install pymongo and dnspython library for Python
import http.server
import socketserver
import pymongo
from bson.json_util import dumps, loads

myclient = pymongo.MongoClient("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["foodHunterDB"]
mycol = mydb["restaurantsExtended"]
#mycol = mydb["restaurants"]

cursor = mycol.find({}, {'_id': False, '__v': False})
list_cur = list(cursor)

# Converting to the JSON
json_data = dumps(list_cur, indent = 2)

# Over-Writing data to file data_food_sample.json
with open('data_food_sample.json', 'w') as file:
    file.write(json_data)

print("Successfully updated JSON from the mongoDB server.")

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is initiated at port", PORT)
    httpd.serve_forever()
