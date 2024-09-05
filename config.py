import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    
    # Additional configuration options can be added as needed, e.g., for external APIs
