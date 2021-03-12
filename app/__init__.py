from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.contrib.fixers import ProxyFix
from flask_restplus import Api

app = Flask(__name__)
app.config.from_object('config')
# app.wsgi_app = ProxyFix(app.wsgi_app)
# blueprint = Blueprint('api', __name__,url_prefix='/api')
# app.register_blueprint(blueprint)


authorizations = {
    'x-access-token': {
        'in': "header",
        'type': "apiKey",
        'description': "Insira o seu Token JWT aqui!"
    }
}

api = Api(app, title='Api Flask', version='1.0', description='Api service com python flask',prefix='/api', authorizations=authorizations)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default