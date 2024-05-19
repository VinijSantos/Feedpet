from routes.landing import landing_route
#from routes.user import user_route
from database.database import db
from database.models.usuario import User


def config_all(app):
    config_routes(app)
    config_db()


def config_routes(app):
    app.register_blueprint(landing_route)
    #app.register_blueprint(user_route, url_prefix='/user')


def config_db():
    db.connect()
    db.create_tables([User])
