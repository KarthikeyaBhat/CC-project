from flask import Flask,flash,redirect
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Subtraction(Resource):
    def get(self,num1,num2):
        result = num1-num2
        flash(f'The result of operation subtraction on {num1} and {num2} is {result}')
        return redirect("/")
    
api.add_resource(Subtraction,"/sub/<int:num1>/<int:num2>")