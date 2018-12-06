from flask import Flask
from flask_restful import Resource, Api, reqparse

# Imports für pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://db:27017") # Wie im docker-compose.yml

# Datenbank erstellen
db = client.aNewDB
UserNum = db["UserNum"]

# Document
UserNum.insert({
    'num_of_users': 0
})

app = Flask(__name__)

api = Api(app)

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users": new_num}})

        return str("Hello User"+ str(new_num))

api.add_resource(Visit, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
