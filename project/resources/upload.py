from flask_restful import Resource
from flask import request
import os
from config import UPLOAD_FOLDER
from model import save_data_in_db


class upload(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    def post(self):
        file = request.files['file']
        if file.filename == '':
            print("NO")
        else:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        save_data_in_db(os.path.join(UPLOAD_FOLDER, file.filename))
        
