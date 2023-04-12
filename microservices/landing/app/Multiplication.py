from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Multiplication(Resource):
    def get(self,num1,num2):
        return str(num1*num2)
    