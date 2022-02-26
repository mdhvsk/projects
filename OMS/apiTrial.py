from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"madhav": {"age": 20, "gender": "male"},
         "abhi": {"age": 21, "gender": "male"}}

class HelloWorld(Resource):
    #pass in dictionary or json format
    def get(self, name):
        return names[name]

    #def post(self):
        #return {"data": "Posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

