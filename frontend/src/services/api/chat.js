import { API_BASE_URL, API_ENDPOINTS } from '../utils/constants';

export const chatService = {
  // Send message
  sendMessage: async (discussionId, message, history = []) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.CHAT(discussionId)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, history }),
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to send message');
    }
    
    return data.data;
  },
};

