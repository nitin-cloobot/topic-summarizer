import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# App logger for general application logs
app_logger = logging.getLogger('app')
app_logger.setLevel(logging.INFO)

# Error logger for errors and exceptions
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# App logger handlers
app_file_handler = RotatingFileHandler(
    'logs/app.log',
    maxBytes=10485760,  # 10MB
    backupCount=5
)
app_file_handler.setFormatter(formatter)
app_logger.addHandler(app_file_handler)

# Console handler for app logger
app_console_handler = logging.StreamHandler()
app_console_handler.setFormatter(formatter)
app_logger.addHandler(app_console_handler)

# Error logger handlers
error_file_handler = RotatingFileHandler(
    'logs/error.log',
    maxBytes=10485760,  # 10MB
    backupCount=5
)
error_file_handler.setFormatter(formatter)
error_logger.addHandler(error_file_handler)

# Console handler for error logger
error_console_handler = logging.StreamHandler()
error_console_handler.setFormatter(formatter)
error_logger.addHandler(error_console_handler)

