from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

from api.controller.car import Car
from api.controller.car import CarList

app = Flask(__name__)

app.config['MONGO_URI'] = ''
app.database = PyMongo(app)
app.cars_collection = app.database.db.cars

api = Api(app)


#...
#...
#...

api.add_resource(Car, '/car', '/car/<car_id>',
                 methods=['GET', 'POST', 'PUT', 'DELETE'])

api.add_resource(CarList, '/cars',
                 methods=['GET'])
