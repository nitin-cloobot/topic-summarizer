from flask import jsonify

def success_response(data=None, message=None, status_code=200):
    """Return a success response"""
    response = {
        'success': True
    }
    if message:
        response['message'] = message
    if data is not None:
        response['data'] = data
    
    return jsonify(response), status_code

def error_response(message, status_code=400, errors=None):
    """Return an error response"""
    response = {
        'success': False,
        'message': message
    }
    if errors:
        response['errors'] = errors
    
    return jsonify(response), status_code

