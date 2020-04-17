from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from api import SITE_API # Set API dev in an another file
from flask_login import LoginManager, UserMixin

#Ceeating the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.register_blueprint(SITE_API)

#Creating the database dor Admin
db = SQLAlchemy()

#Construction of the class Admin
class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#App initialisation for login
def create_app():
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Admin.query.get(int(user_id))

     # blueprint for auth routes in our app
    #app.register_blueprint(app_blueprint)

    return app

