from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self):
        return {'info' : 'Hello world', 'num': 54}


api.add_resource(Quote, '/api/main')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')    

