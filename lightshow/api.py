from flask import jsonify
from flask_restful import Api, Resource

from .app import app
from .lightshow import lightshow


class LightshowApi(Resource):
    def get(self, index, value):
        pass


api = Api(app)
api.add_resource(LightshowApi, "/api/<int:index>/<str:value>")
