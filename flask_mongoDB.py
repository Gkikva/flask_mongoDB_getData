from flask import Flask , render_template
from pymongo import MongoClient


app = Flask(__name__)


MONGO_USER = "firstUser"
MONGO_PASS = "firstUserfirstUser"

client = MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.beibl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
simple_db = client.get_database("sample_analytics")
company_db = simple_db.customers
lists = list(company_db.find())
user_list = []

print(user_list)
for ll in lists:
        list_dict = {}
        list_dict["name"] = ll["name"]
        list_dict["address"] = ll["address"]
        list_dict["email"] = ll["email"]

        user_list.append(list_dict)
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/all")
def all():

        return render_template("all.html" , user_list = user_list)


