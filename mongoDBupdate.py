# Citation (IEEE FORMATTED)
# pymongo, Tutorial. N/A: pymongo, NA [webpage]
# https://pymongo.readthedocs.io/en/stable/tutorial.html

import requests
import json
import math
import pymongo
import re

# Citation (IEEE FORMATTED)
# Documenu, Getting Started. N/A: Documenu, N/A. [webpage].
# https://documenu.com/docs#get_search_restaurants_geo

key = "a7e037de3731e07c5ad9ebbaedcf25da";
#The centre is University of Washington acc to lat and lon
lat = "47.655548";
lon = "-122.303200";
#Radius acc to the centre
dist = "1";
url = "https://api.documenu.com/v2/restaurants/search/geo?lat="+lat+"&lon="+lon+"&distance="+dist+"&fullmenu&key="+key;

r =requests.get(url)

d_dict = r.json()

#print(d_dict["data"][0]["restaurant_name"])
totalRest = d_dict["totalResults"]
totalPage = math.ceil(totalRest/25)
totalPage = totalPage+1;

mongo_list = []
#For the sake of database tests
test={
"restaurant": "restaurantTest",
"product": "productTest",
"ingredients": "ing1, ing2, ing3",
"tags": "",
"address": "adressTest"
}
#For the sake of location tests
test2={
    "restaurant": "Starbucks",
    "product": "Sausage, Cheddar & Egg Sandwich",
    "ingredients": "sausage,egg,cheese,english muffin",
    "tags": "nonveg, fast food, breakfast",
    "address": "200 University Ave W, Waterloo, ON N2L 3G1"
}
mongo_list.append(test)
mongo_list.append(test2)

#tag is a duplication of ingredients, however I keep it because of the backend tests
for page in range(1,totalPage):
    url = "https://api.documenu.com/v2/restaurants/search/geo?lat="+lat+"&lon="+lon+"&distance="+dist+"&page="+str(page)+"&fullmenu&key="+key;
    r =requests.get(url)
    d_dict = r.json()
    for i in d_dict["data"]:
        for j in i["menus"]:
            if(j["menu_name"] == "Main"):
                for k in j["menu_sections"]:
                    for l in k["menu_items"]:
                        dish={
                        "restaurant": i["restaurant_name"],
                        "product": l["name"],
                        "ingredients": re.sub("[ .;:]", ",", l["description"].lower()),
                        "tags": "",
                        "address": i["address"]["formatted"]
                        # "price": l["price"]
                        }
                        mongo_list.append(dish)
    print("Page "+str(page)+" is completed, numbe of total page is: "+str(totalPage))

myclient = pymongo.MongoClient("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["foodHunterDB"]
mycol = mydb["restaurantsExtended"]

#Instead of checking and updateding the changed things, I delete and rewrite
print("Deleting the old tables")
mycol.drop()
mycol.insert_many(mongo_list)
print("MongoDB (foodHunterDB/restaurantsExtended) is updated")

#print( len(mongo_list) )
#print(d_dict["data"][0]["menus"])

# for i in d_dict["data"]:
#     print(i["address"]["formatted"])
