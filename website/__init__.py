# Import modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create database
db = SQLAlchemy()
DB_NAME = "database.db"

# Initiate website and database


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd5DrWBqQS1OmC6XE'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

# Import views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Faq  # Import models for database

# If database doesn't exist create database
    with app.app_context():
        db.create_all()
        print("Created database!")

# Use auth and login to login users
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
