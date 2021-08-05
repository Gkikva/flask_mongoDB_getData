from pymongo import MongoClient
from pprint import pprint
from tqdm import tqdm
import json
MONGO_USER = "firstUser"
MONGO_PASS = "firstUserfirstUser"

client = MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.beibl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

simple_db = client.get_database("sample_analytics")

company_db = simple_db.customers
lists = list(company_db.find())

users_list = []
for ll in tqdm(lists):
    list_dict = {}
    list_dict["name"] = ll["name"]
    list_dict["address"] = ll["address"]
    list_dict["email"] = ll["email"]

    users_list.append(list_dict)


for users in users_list:
    print(users)
