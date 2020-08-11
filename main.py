from flask import Flask, request
from flask_cors import CORS
from flask_restplus import fields, Api, Resource

from service.Service import Service

flask_app = Flask(__name__)
CORS(flask_app)
api = Api(
    app=flask_app,
    version="1.0",
    title="example swagger",
    description="description example"
)

# param swagger
param_transform = api.model('paramExample', {
    "name": fields.String()
})


# grouping
name_space = api.namespace('', description='TEST API')


@name_space.route("/")
class TransformClass(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(param_transform)
    def post(self):
        param = request.get_json()
        data = Service().getName(param["name"])
        return data


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=1234)
