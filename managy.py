from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from configs.app import app
from configs.db import db

# Import the models defiend, to be convert to table schema
from  models.plan import Plan

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()