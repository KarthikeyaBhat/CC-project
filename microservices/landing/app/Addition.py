from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Addition(Resource):
    def get(self,num1,num2):
        print(str(num1+num2))
    