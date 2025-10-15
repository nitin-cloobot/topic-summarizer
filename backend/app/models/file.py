import sqlite3
from datetime import datetime
from logging_config import app_logger, error_logger

class File:
    """File model for managing file records"""
    
    @staticmethod
    def create(db_path, discussion_id, filename, file_path, file_size):
        """Create a new file record"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO Files (discussion_id, filename, file_path, file_size, uploaded_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (discussion_id, filename, file_path, file_size, datetime.now()))
            
            file_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            app_logger.info(f"File record created with ID: {file_id}")
            return file_id
        except Exception as e:
            error_logger.error(f"Error creating file record: {e}", exc_info=True)
            raise
    
    @staticmethod
    def get_by_discussion(db_path, discussion_id):
        """Get all files for a discussion"""
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, discussion_id, filename, file_path, file_size, uploaded_at
                FROM Files
                WHERE discussion_id = ?
                ORDER BY uploaded_at DESC
            ''', (discussion_id,))
            
            files = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            app_logger.info(f"Retrieved {len(files)} files for discussion {discussion_id}")
            return files
        except Exception as e:
            error_logger.error(f"Error fetching files for discussion {discussion_id}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def count_by_discussion(db_path, discussion_id):
        """Count files in a discussion"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM Files WHERE discussion_id = ?', (discussion_id,))
            count = cursor.fetchone()[0]
            conn.close()
            
            return count
        except Exception as e:
            error_logger.error(f"Error counting files for discussion {discussion_id}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def delete(db_path, file_id):
        """Delete a file record"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM Files WHERE id = ?', (file_id,))
            
            conn.commit()
            conn.close()
            
            app_logger.info(f"File deleted: {file_id}")
            return True
        except Exception as e:
            error_logger.error(f"Error deleting file {file_id}: {e}", exc_info=True)
            raise

