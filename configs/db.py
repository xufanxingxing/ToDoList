from flask_sqlalchemy import SQLAlchemy
from configs.app import app


db = SQLAlchemy(app)
