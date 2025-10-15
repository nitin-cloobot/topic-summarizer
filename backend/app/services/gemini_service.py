import os
import requests
from logging_config import app_logger, error_logger

class GeminiService:
    """Service for interacting with Gemini LLM API"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('LLM_API_KEY')
        self.endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
    
    def get_chat_response(self, user_message, context_chunks=None, history=None):
        """
        Get AI response for a chat message with document context
        
        Args:
            user_message: The user's question
            context_chunks: List of document chunks for context
            history: Previous conversation history
        
        Returns:
            AI response text
        """
        
        # Build system prompt with document context
        system_prompt = """You are an AI assistant that helps users understand and analyze their documents.

Your task is to:
1. Answer questions based on the provided document content.
2. Provide clear, concise, and accurate responses.
3. Cite specific information from the documents when relevant.
4. If the answer is not in the documents, clearly state that.
5. Be helpful, professional, and easy to understand.

Important Rules:
- Always base your answers on the provided document content.
- Do not make up information that is not in the documents.
- If you're unsure, acknowledge the uncertainty.
- Keep responses focused and relevant to the user's question.
"""
        
        # Add document context to system prompt if available
        if context_chunks and len(context_chunks) > 0:
            context_text = "\n\n--- Document Content ---\n\n"
            for chunk in context_chunks:
                context_text += f"{chunk.get('content', '')}\n\n"
            context_text += "--- End of Document Content ---\n"
            system_prompt += context_text
        
        headers = {
            'Content-Type': 'application/json',
            'x-goog-api-key': self.api_key
        }
        
        # Build the contents list
        contents = []
        if history:
            contents.extend(history)
        
        # Add the current user message
        contents.append({"role": "user", "parts": [{"text": user_message}]})
        
        payload = {
            "system_instruction": {
                "parts": [{"text": system_prompt}]
            },
            "contents": contents
        }
        
        try:
            app_logger.info(f"Sending request to Gemini API")
            response = requests.post(self.endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            ai_text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            app_logger.info(f"Gemini API response generated successfully")
            return ai_text
        except Exception as e:
            error_logger.error(f"Gemini API Error: {e}", exc_info=True)
            return f"[AI Error]: Unable to generate response. Please try again."

