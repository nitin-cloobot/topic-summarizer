from flask import Blueprint, request, current_app
from app.models.discussion import Discussion
from app.models.file_chunk import FileChunk
from app.services.gemini_service import GeminiService
from app.utils.response_helpers import success_response, error_response
from logging_config import app_logger, error_logger

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/<int:discussion_id>/chat', methods=['POST'])
def send_message(discussion_id):
    """Send a message to the AI chat"""
    try:
        db_path = current_app.config['DATABASE_PATH']
        
        # Check if discussion exists
        discussion = Discussion.get_by_id(db_path, discussion_id)
        if not discussion:
            return error_response("Discussion not found", status_code=404)
        
        # Get request data
        data = request.get_json()
        if not data or 'message' not in data:
            return error_response("Message is required", status_code=400)
        
        user_message = data['message'].strip()
        if not user_message:
            return error_response("Message cannot be empty", status_code=400)
        
        history = data.get('history', [])
        
        # Get all chunks for this discussion
        chunks = FileChunk.get_by_discussion(db_path, discussion_id)
        
        if len(chunks) == 0:
            return error_response(
                "No files uploaded yet. Please upload documents before chatting.",
                status_code=400
            )
        
        # Initialize Gemini service
        gemini_service = GeminiService(current_app.config['LLM_API_KEY'])
        
        # Get AI response
        try:
            ai_response = gemini_service.get_chat_response(
                user_message=user_message,
                context_chunks=chunks,
                history=history
            )
            
            return success_response(
                data={
                    'message': ai_response,
                    'chunks_used': len(chunks)
                }
            )
        except Exception as ai_error:
            error_logger.error(f"AI service error: {ai_error}", exc_info=True)
            return error_response(
                "Failed to generate AI response. Please try again.",
                status_code=500
            )
        
    except Exception as e:
        error_logger.error(f"Error in send_message: {e}", exc_info=True)
        return error_response("Failed to process chat message", status_code=500)

