from flask import Flask, request
from flask_restful import Api, Resource
from pymongo import MongoClient

# connecting to MongoDB and my database
cluster = MongoClient("mongodb+srv://aras:aras8888@pythoncluster.k0toj45.mongodb.net/?retryWrites=true&w=majority")
db = cluster['school_epo']
collection = db['info']

# starting Flask server
app = Flask(__name__)
api = Api(app)


# create an api which can directly make change to a specific person
class School_info(Resource):
    def get(self, _id):
        person = collection.find_one({'_id': int(_id)})
        return person, 200 if person is not None else 404

    def put(self, _id):
        data = request.get_json()
        info_update = collection.update_one({'_id': int(_id)}, {'$set': {'name': data['name'],
                                                                         'ID': data['ID'],
                                                                         'DEPT': data['DEPT']}})
        return info_update, 201 if info_update['message'] != "Internal Server Error" else 404

    def delete(self, _id):
        result = collection.delete_one({'_id': int(_id)})
        print(result)
        return result, 201 if result['message'] != "Internal Server Error" else 404


# create an api which can make change to all data, or post new data to the database
class all_info(Resource):
    def get(self):
        cursor = collection.find({})
        list_cur = list(cursor)
        return list_cur

    def post(self):
        data = request.get_json()
        if collection.find_one({'ID': data['ID']}) is not None:
            print(collection.find({'ID': data['ID']}))
            return {'message': f'An item with ID {data["ID"]} already exists.'}, 400

        person = {
            '_id': data['_id'],
            'name': data['name'],
            'ID': data['ID'],
            'DEPT': data['DEPT']
        }
        collection.insert_one(person)
        return person, 201

    def delete(self):
        collection.delete_many({})
        return {"message": "All info have been deleted."}


# implementing my restapi
api.add_resource(School_info, '/info/<_id>')
api.add_resource(all_info, '/infos')

# let my server run directly
if __name__ == '__main__':
    app.run(debug=False)
