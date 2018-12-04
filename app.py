from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

_parser = reqparse.RequestParser()
_parser.add_argument('x', type=float, required=True, help='X must be provided and float') #, help='X must be provided and float'
_parser.add_argument('y', type=float, required=True, help='Y must be provided and float')

class Plus(Resource):
    def post(self):
        data = _parser.parse_args()
        result = data['x'] + data['y']
        return {'result': result}, 200

class Sub(Resource):
    def post(self):
        data = _parser.parse_args()
        result = data['x'] - data['y']
        return {'result': result}, 200

class Div(Resource):
    def post(self):
        data = _parser.parse_args()
        if data['y'] == 0:
            return {'Error': 'y kleinergleich 0'}, 301
        result = data['x'] / data['y']
        return {'result': result}, 200

class Mul(Resource):
    def post(self):
        data = _parser.parse_args()
        result = data['x'] * data['y']
        return {'result': result}, 200


api.add_resource(Plus, '/plus')
api.add_resource(Sub, '/sub')
api.add_resource(Div, '/div')
api.add_resource(Mul, '/mul')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
