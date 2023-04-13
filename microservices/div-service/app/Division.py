from flask import Flask,flash,redirect
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Division(Resource):
    def get(self,num1,num2):
        if(num2==0):
            result = "undefined"
        else:  
            result = num1/num2
        flash(f'The result of operation division on {num1} and {num2} is {result}')
        return redirect("/")
    
api.add_resource(Division,"/div/<int:num1>/<int:num2>")