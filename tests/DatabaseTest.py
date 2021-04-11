import unittest
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["foodHunterDB"]
mycol = mydb["restaurantsExtended"]


def test1():
    #check if the db is available
    try:
        myclient.server_info()
        return True
    except:
        return False

def test2():
    #Check if the most basic query can be menu_items
    testData = mycol.find_one({"restaurant": "restaurantTest"})
    return testData['product'] == "productTest"

def test3():
    testData = mycol.find({})
    #There is more than test object
    return testData.count() > 1



class DBTest(unittest.TestCase):
    @classmethod

    def test_db_connection(self):
        assert test1(), "\nmongoDB server is not available!"

    def test_db_dataAvalilability(self):
        assert test2(), "\nrestaurantsExtended collection is not available!"

    def test_db_dataCorrruption(self):
        assert test3(), "\nrestaurantsExtended collection is corrupted!"
