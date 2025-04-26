"""
Main Flask Application Initialization
"""

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from application.database import db
import config
from application.bp.homepage import bp_homepage
from application.bp.authentication import authentication

migrate = Migrate()
csrf = CSRFProtect()
bootstrap = Bootstrap5()

def init_app():
    """
    Initialize the core application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    # Initialize Plugins
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    with app.app_context():
        blueprints = [bp_homepage, authentication]
        for blueprint in blueprints:
            app.register_blueprint(blueprint)

        return app
