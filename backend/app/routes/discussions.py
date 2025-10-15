from flask import Blueprint, request, current_app
from app.models.discussion import Discussion
from app.utils.response_helpers import success_response, error_response
from logging_config import app_logger, error_logger

discussions_bp = Blueprint('discussions', __name__)

@discussions_bp.route('', methods=['GET'])
def get_discussions():
    """Get all discussions"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        discussions = Discussion.get_all(db_path)
        return success_response(data=discussions)
    except Exception as e:
        error_logger.error(f"Error in get_discussions: {e}", exc_info=True)
        return error_response("Failed to fetch discussions", status_code=500)

@discussions_bp.route('/<int:discussion_id>', methods=['GET'])
def get_discussion(discussion_id):
    """Get a specific discussion"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        discussion = Discussion.get_by_id(db_path, discussion_id)
        
        if not discussion:
            return error_response("Discussion not found", status_code=404)
        
        return success_response(data=discussion)
    except Exception as e:
        error_logger.error(f"Error in get_discussion: {e}", exc_info=True)
        return error_response("Failed to fetch discussion", status_code=500)

@discussions_bp.route('', methods=['POST'])
def create_discussion():
    """Create a new discussion"""
    try:
        data = request.get_json()
        
        if not data or 'name' not in data:
            return error_response("Discussion name is required", status_code=400)
        
        name = data['name'].strip()
        if not name:
            return error_response("Discussion name cannot be empty", status_code=400)
        
        description = data.get('description', '').strip()
        
        db_path = current_app.config['DATABASE_PATH']
        discussion_id = Discussion.create(db_path, name, description if description else None)
        
        # Fetch the created discussion
        discussion = Discussion.get_by_id(db_path, discussion_id)
        
        return success_response(
            data=discussion,
            message="Discussion created successfully",
            status_code=201
        )
    except Exception as e:
        error_logger.error(f"Error in create_discussion: {e}", exc_info=True)
        return error_response("Failed to create discussion", status_code=500)

@discussions_bp.route('/<int:discussion_id>', methods=['PUT'])
def update_discussion(discussion_id):
    """Update a discussion"""
    try:
        data = request.get_json()
        
        if not data:
            return error_response("No data provided", status_code=400)
        
        name = data.get('name', '').strip() if 'name' in data else None
        description = data.get('description', '').strip() if 'description' in data else None
        
        if name is not None and not name:
            return error_response("Discussion name cannot be empty", status_code=400)
        
        db_path = current_app.config['DATABASE_PATH']
        success = Discussion.update(db_path, discussion_id, name, description)
        
        if not success:
            return error_response("Discussion not found", status_code=404)
        
        # Fetch updated discussion
        discussion = Discussion.get_by_id(db_path, discussion_id)
        
        return success_response(
            data=discussion,
            message="Discussion updated successfully"
        )
    except Exception as e:
        error_logger.error(f"Error in update_discussion: {e}", exc_info=True)
        return error_response("Failed to update discussion", status_code=500)

@discussions_bp.route('/<int:discussion_id>', methods=['DELETE'])
def delete_discussion(discussion_id):
    """Delete a discussion"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        
        # Check if discussion exists
        discussion = Discussion.get_by_id(db_path, discussion_id)
        if not discussion:
            return error_response("Discussion not found", status_code=404)
        
        # Delete discussion
        Discussion.delete(db_path, discussion_id)
        
        return success_response(message="Discussion deleted successfully")
    except Exception as e:
        error_logger.error(f"Error in delete_discussion: {e}", exc_info=True)
        return error_response("Failed to delete discussion", status_code=500)

