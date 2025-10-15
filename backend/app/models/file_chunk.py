import sqlite3
from datetime import datetime
from logging_config import app_logger, error_logger

class FileChunk:
    """FileChunk model for managing file chunk records"""
    
    @staticmethod
    def create(db_path, file_id, chunk_index, content):
        """Create a new file chunk"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO FileChunks (file_id, chunk_index, content, created_at)
                VALUES (?, ?, ?, ?)
            ''', (file_id, chunk_index, content, datetime.now()))
            
            chunk_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return chunk_id
        except Exception as e:
            error_logger.error(f"Error creating file chunk: {e}", exc_info=True)
            raise
    
    @staticmethod
    def create_batch(db_path, file_id, chunks):
        """Create multiple chunks for a file"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            chunk_data = [(file_id, idx, content, datetime.now()) for idx, content in enumerate(chunks)]
            
            cursor.executemany('''
                INSERT INTO FileChunks (file_id, chunk_index, content, created_at)
                VALUES (?, ?, ?, ?)
            ''', chunk_data)
            
            conn.commit()
            conn.close()
            
            app_logger.info(f"Created {len(chunks)} chunks for file {file_id}")
            return True
        except Exception as e:
            error_logger.error(f"Error creating batch chunks: {e}", exc_info=True)
            raise
    
    @staticmethod
    def get_by_file(db_path, file_id):
        """Get all chunks for a file"""
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, file_id, chunk_index, content, created_at
                FROM FileChunks
                WHERE file_id = ?
                ORDER BY chunk_index ASC
            ''', (file_id,))
            
            chunks = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            return chunks
        except Exception as e:
            error_logger.error(f"Error fetching chunks for file {file_id}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def get_by_discussion(db_path, discussion_id):
        """Get all chunks for all files in a discussion"""
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT fc.id, fc.file_id, fc.chunk_index, fc.content, fc.created_at, f.filename
                FROM FileChunks fc
                JOIN Files f ON fc.file_id = f.id
                WHERE f.discussion_id = ?
                ORDER BY f.id ASC, fc.chunk_index ASC
            ''', (discussion_id,))
            
            chunks = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            app_logger.info(f"Retrieved {len(chunks)} chunks for discussion {discussion_id}")
            return chunks
        except Exception as e:
            error_logger.error(f"Error fetching chunks for discussion {discussion_id}: {e}", exc_info=True)
            raise

