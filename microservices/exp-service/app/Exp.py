from flask import Flask,flash, render_template,redirect,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


class Exp(Resource):
    @app.route("/exp/<int:num1>/<int:num2>",methods=["GET"])
    def get(num1,num2):
        result = num1**num2
        flash(f'The result of operation exponent on {num1} and {num2} is {result}')
        return jsonify(result)
    
api.add_resource(Exp,"/localhost:5080/exp/<int:num1>/<int:num2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
    
    #/add/<int:num1>/<int:num2>