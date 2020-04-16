from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

from models import Admin
from flask_login import LoginManager
def create_app():

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Admin.query.get(int(user_id))

     # blueprint for auth routes in our app
    from app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app