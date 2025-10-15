import sqlite3
import os
from logging_config import app_logger, error_logger

def init_db(db_path):
    """Initialize the SQLite database with schema"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create Discussions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Discussions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create Files table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discussion_id INTEGER NOT NULL,
                filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                file_size INTEGER,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (discussion_id) REFERENCES Discussions(id) ON DELETE CASCADE
            )
        ''')
        
        # Create FileChunks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS FileChunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                chunk_index INTEGER NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (file_id) REFERENCES Files(id) ON DELETE CASCADE
            )
        ''')
        
        # Create indexes for better query performance
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_discussion_id ON Files(discussion_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_chunks_file_id ON FileChunks(file_id)')
        
        conn.commit()
        conn.close()
        
        app_logger.info(f"Database initialized successfully at {db_path}")
        return True
    except Exception as e:
        error_logger.error(f"Error initializing database: {e}", exc_info=True)
        raise

def get_db_connection(db_path):
    """Get a database connection"""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        # Enable foreign key support
        conn.execute('PRAGMA foreign_keys = ON')
        return conn
    except Exception as e:
        error_logger.error(f"Error connecting to database: {e}", exc_info=True)
        raise

