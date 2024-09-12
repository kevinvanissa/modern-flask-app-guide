from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instantiate extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):

    # Create a new flask instance
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Initialize the extension libraries with application
    db.init_app(app)
    migrate.init_app(app, db)

    #Register blueprints
    from .views import main_bp
    from .views import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app
