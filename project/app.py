from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.upload import upload

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(upload, '/upload')