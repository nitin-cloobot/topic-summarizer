import os
import requests
import logging
from logging_config import app_logger, error_logger

def get_gemini_response(user_message, history=None):
    """
    Sends a chat message to Gemini 2.5 Flash API and returns the AI response text.
    """

    system_prompt = """You are an AI assistant that specializes in requirement gap clarification for Salesforce implementation projects.  

        Your task is to:
        1. Take the requirement document provided by the user.
        2. Carefully analyze it for missing details, contradictions, ambiguities, or unclear points.
        3. Present these issues to the user one at a time in a numbered format:
        - Start with "Gap 1:" followed by the question.
        - After asking each question, wait for the user’s response before moving to the next gap.
        - Do not ask multiple gaps in the same turn.
        4. When the user answers, acknowledge their clarification briefly (e.g., “Got it. Thanks for clarifying.”) and then continue with the next gap.
        5. If all gaps are clarified, provide a **final summarized version** of the clarified requirements.

        Important Rules:
        - Always stay in context of Salesforce implementation (Sales Cloud, Service Cloud, custom objects, workflows, dashboards, etc.).
        - Phrase questions in a way that a business analyst or consultant would, aiming to capture precise requirements.
        - Do not generate code or technical solutions — focus only on clarifying the requirement.
        - Keep responses concise, professional, and easy for a non-technical stakeholder to understand.
    """

    api_key = os.getenv('LLM_API_KEY')
    endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': api_key
    }
    # Build the contents list, starting with history if provided
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
        app_logger.info(f"Gemini API user message recieved")
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        ai_text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        app_logger.info(f"Gemini API response generated")
        return ai_text
    except Exception as e:
        error_logger.error(f"Gemini API Error: {e}", exc_info=True)
        return f"[Gemini API Error]: {str(e)}"
