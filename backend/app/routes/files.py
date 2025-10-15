from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename
import os
from app.models.discussion import Discussion
from app.models.file import File
from app.models.file_chunk import FileChunk
from app.services.file_processor import FileProcessor
from app.utils.validators import validate_file_upload, sanitize_filename
from app.utils.response_helpers import success_response, error_response
from logging_config import app_logger, error_logger

files_bp = Blueprint('files', __name__)

@files_bp.route('/<int:discussion_id>/files', methods=['GET'])
def get_files(discussion_id):
    """Get all files for a discussion"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        
        # Check if discussion exists
        discussion = Discussion.get_by_id(db_path, discussion_id)
        if not discussion:
            return error_response("Discussion not found", status_code=404)
        
        files = File.get_by_discussion(db_path, discussion_id)
        return success_response(data=files)
    except Exception as e:
        error_logger.error(f"Error in get_files: {e}", exc_info=True)
        return error_response("Failed to fetch files", status_code=500)

@files_bp.route('/<int:discussion_id>/files', methods=['POST'])
def upload_files(discussion_id):
    """Upload files to a discussion"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        
        # Check if discussion exists
        discussion = Discussion.get_by_id(db_path, discussion_id)
        if not discussion:
            return error_response("Discussion not found", status_code=404)
        
        # Check if files are in request
        if 'files' not in request.files:
            return error_response("No files provided", status_code=400)
        
        files = request.files.getlist('files')
        if not files or len(files) == 0:
            return error_response("No files selected", status_code=400)
        
        # Check file count limit
        current_file_count = File.count_by_discussion(db_path, discussion_id)
        max_files = current_app.config['MAX_FILES_PER_DISCUSSION']
        
        if current_file_count + len(files) > max_files:
            return error_response(
                f"File limit exceeded. Maximum {max_files} files per discussion. "
                f"Currently {current_file_count} files uploaded.",
                status_code=400
            )
        
        # Process each file
        uploaded_files = []
        errors = []
        
        for file in files:
            try:
                # Validate file
                is_valid, error_msg = validate_file_upload(file, current_app.config['MAX_FILE_SIZE'])
                if not is_valid:
                    errors.append({
                        'filename': file.filename,
                        'error': error_msg
                    })
                    continue
                
                # Save file
                filename = sanitize_filename(file.filename)
                discussion_folder = os.path.join(
                    current_app.config['UPLOAD_FOLDER'],
                    f"discussion_{discussion_id}"
                )
                os.makedirs(discussion_folder, exist_ok=True)
                
                file_path = os.path.join(discussion_folder, filename)
                
                # Handle duplicate filenames
                counter = 1
                base_name, ext = os.path.splitext(filename)
                while os.path.exists(file_path):
                    filename = f"{base_name}_{counter}{ext}"
                    file_path = os.path.join(discussion_folder, filename)
                    counter += 1
                
                file.save(file_path)
                file_size = os.path.getsize(file_path)
                
                # Create file record
                file_id = File.create(db_path, discussion_id, filename, file_path, file_size)
                
                # Process file and create chunks
                try:
                    chunks = FileProcessor.process_file(file_path)
                    FileChunk.create_batch(db_path, file_id, chunks)
                    
                    uploaded_files.append({
                        'id': file_id,
                        'filename': filename,
                        'size': file_size,
                        'chunks': len(chunks)
                    })
                except Exception as proc_error:
                    error_logger.error(f"Error processing file {filename}: {proc_error}", exc_info=True)
                    errors.append({
                        'filename': filename,
                        'error': f"Failed to process file: {str(proc_error)}"
                    })
                    # Delete file record if processing failed
                    File.delete(db_path, file_id)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                
            except Exception as file_error:
                error_logger.error(f"Error uploading file: {file_error}", exc_info=True)
                errors.append({
                    'filename': file.filename if file else 'unknown',
                    'error': str(file_error)
                })
        
        # Return response
        if len(uploaded_files) == 0 and len(errors) > 0:
            return error_response(
                "Failed to upload any files",
                status_code=400,
                errors=errors
            )
        
        response_data = {
            'uploaded': uploaded_files,
            'count': len(uploaded_files)
        }
        
        if errors:
            response_data['errors'] = errors
        
        return success_response(
            data=response_data,
            message=f"Successfully uploaded {len(uploaded_files)} file(s)",
            status_code=201
        )
        
    except Exception as e:
        error_logger.error(f"Error in upload_files: {e}", exc_info=True)
        return error_response("Failed to upload files", status_code=500)

