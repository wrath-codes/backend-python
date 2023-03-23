from flask import Flask
from flask_cors import CORS

from src.main.routes import api_routes_bp

app = Flask(__name__)

# Enable CORS
CORS(app)

# Registering Blueprints
app.register_blueprint(api_routes_bp)
