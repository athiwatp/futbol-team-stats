from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

db = SQLAlchemy()
ma = Marshmallow()
api = Api()

from flask_login import LoginManager

# Login Manager
login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"
