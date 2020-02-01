from website import flaskApp, db
from website.models import Post, User, Project
from website.database import Dbase




@flaskApp.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Project': Project, 'Dbase': Dbase}