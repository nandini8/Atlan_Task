import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.path.join(basedir, 'database/database.db')
UPLOAD_FOLDER = os.path.join(basedir, 'upload_folder')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False