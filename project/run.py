from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

database = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    database.init_app(app)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    with app.app_context():
        database.create_all()
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
