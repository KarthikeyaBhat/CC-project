from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api
import requests
import os
from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division


app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

api.add_resource(Addition,"/add/<int:num1>/<int:num2>")
api.add_resource(Subtraction,"/sub/<int:num1>/<int:num2>")
api.add_resource(Multiplication,"/mul/<int:num1>/<int:num2>")
api.add_resource(Division,"/div/<int:num1>/<int:num2>")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=="POST":
        num1 = request.form.get("first",type=int)
        num2 = request.form.get('second',type=int)
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            api.add_resource(Addition,"/add/<int:{}>/<int:{num2:%d}>".format(num1,num2))
        # elif operation == 'minus':
        #     result =  sub(number_1, number_2)
        # elif operation == 'multiply':
        #     result = mul(number_1, number_2)
        # elif operation == 'divide':
        #     result = div(number_1, number_2)
        # if operation == 'add':
        #     return redirect("localhost:5050/add/<int:{num1}>/<int:{num2}>")
        # elif operation == 'minus':
        #     return redirect("localhost:5050/sub/<int:{num1}>/<int:{num2}>")
        # elif operation == 'multiply':
        #     return redirect("localhost:5050/mul/<int:{num1}>/<int:{num2}>")
        # elif operation == 'divide':
        #     return redirect("localhost:5050/div/<int:{num1}>/<int:{num2}>")

        # flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        # return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )