from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    """Factory function to create Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['DATABASE_PATH'] = os.getenv('DATABASE_PATH', 'database/instance/app.db')
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
    app.config['MAX_FILE_SIZE'] = int(os.getenv('MAX_FILE_SIZE', 52428800))  # 50MB
    app.config['MAX_FILES_PER_DISCUSSION'] = int(os.getenv('MAX_FILES_PER_DISCUSSION', 30))
    app.config['LLM_API_KEY'] = os.getenv('LLM_API_KEY', '')
    
    # Configure CORS
    allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000,http://localhost:5173').split(',')
    CORS(app, resources={
        r"/api/*": {
            "origins": allowed_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Create necessary directories
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.dirname(app.config['DATABASE_PATH']), exist_ok=True)
    
    # Initialize database
    from app.services.database_service import init_db
    init_db(app.config['DATABASE_PATH'])
    
    # Register blueprints
    from app.routes.discussions import discussions_bp
    from app.routes.files import files_bp
    from app.routes.chat import chat_bp
    
    app.register_blueprint(discussions_bp, url_prefix='/api/discussions')
    app.register_blueprint(files_bp, url_prefix='/api/discussions')
    app.register_blueprint(chat_bp, url_prefix='/api/discussions')
    
    # Health check route
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy', 'message': 'API is running'}, 200
    
    return app

