from flask import Flask
from models.events_model import db
if __name__ == '__main__':
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
    db.init_app(app)
    app.app_context().push()
    db.create_all()
