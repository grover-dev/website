from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
#from flask_cache import Cache, caching is currently broken


#main initialization
flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
bootstrap = Bootstrap(flaskApp)
db = SQLAlchemy(flaskApp)
#cache = Cache(flaskApp)

migrate = Migrate(flaskApp, db)

manager = Manager(flaskApp)
manager.add_command('db', MigrateCommand)
    
from website import models, database
database.Dbase()
db.create_all()
db.session.commit()

from website import routes

if __name__ == "__main__":    
    manager.run()
    flaskApp.run(debug=True)