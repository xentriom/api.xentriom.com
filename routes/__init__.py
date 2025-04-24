from routes.route import bp as home_bp
from routes.demo.users.route import bp as demo_users_bp

def register(app):
  """Register all routes to the app."""
  
  app.register_blueprint(home_bp)
  app.register_blueprint(demo_users_bp)
