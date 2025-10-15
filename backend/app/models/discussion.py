import sqlite3
from datetime import datetime
from logging_config import app_logger, error_logger

class Discussion:
    """Discussion model for managing discussion records"""
    
    @staticmethod
    def create(db_path, name, description=None):
        """Create a new discussion"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO Discussions (name, description, created_at, updated_at)
                VALUES (?, ?, ?, ?)
            ''', (name, description, datetime.now(), datetime.now()))
            
            discussion_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            app_logger.info(f"Discussion created with ID: {discussion_id}")
            return discussion_id
        except Exception as e:
            error_logger.error(f"Error creating discussion: {e}", exc_info=True)
            raise
    
    @staticmethod
    def get_all(db_path):
        """Get all discussions"""
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, description, created_at, updated_at
                FROM Discussions
                ORDER BY updated_at DESC
            ''')
            
            discussions = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            app_logger.info(f"Retrieved {len(discussions)} discussions")
            return discussions
        except Exception as e:
            error_logger.error(f"Error fetching discussions: {e}", exc_info=True)
            raise
    
    @staticmethod
    def get_by_id(db_path, discussion_id):
        """Get a discussion by ID"""
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, description, created_at, updated_at
                FROM Discussions
                WHERE id = ?
            ''', (discussion_id,))
            
            discussion = cursor.fetchone()
            conn.close()
            
            if discussion:
                app_logger.info(f"Retrieved discussion ID: {discussion_id}")
                return dict(discussion)
            else:
                app_logger.warning(f"Discussion not found: {discussion_id}")
                return None
        except Exception as e:
            error_logger.error(f"Error fetching discussion {discussion_id}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def update(db_path, discussion_id, name=None, description=None):
        """Update a discussion"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get current discussion
            cursor.execute('SELECT name, description FROM Discussions WHERE id = ?', (discussion_id,))
            current = cursor.fetchone()
            
            if not current:
                conn.close()
                return False
            
            # Update with new values or keep current
            new_name = name if name is not None else current[0]
            new_description = description if description is not None else current[1]
            
            cursor.execute('''
                UPDATE Discussions
                SET name = ?, description = ?, updated_at = ?
                WHERE id = ?
            ''', (new_name, new_description, datetime.now(), discussion_id))
            
            conn.commit()
            conn.close()
            
            app_logger.info(f"Discussion updated: {discussion_id}")
            return True
        except Exception as e:
            error_logger.error(f"Error updating discussion {discussion_id}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def delete(db_path, discussion_id):
        """Delete a discussion (cascade deletes files and chunks)"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM Discussions WHERE id = ?', (discussion_id,))
            
            conn.commit()
            conn.close()
            
            app_logger.info(f"Discussion deleted: {discussion_id}")
            return True
        except Exception as e:
            error_logger.error(f"Error deleting discussion {discussion_id}: {e}", exc_info=True)
            raise

