from flask import Blueprint
from flask_restful import Api
from resources.upload import upload
from resources.download import download


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(upload, '/upload')
api.add_resource(download, '/download')