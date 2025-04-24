from flask import Flask
from routes import register

def create_app():
    """Create a Flask app."""
    
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Register all routes
    register(app)

    return app

app = create_app()