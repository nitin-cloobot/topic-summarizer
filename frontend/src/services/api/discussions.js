import { API_BASE_URL, API_ENDPOINTS } from '../utils/constants';

export const discussionService = {
  // Get all discussions
  getAll: async () => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.DISCUSSIONS}`);
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to fetch discussions');
    }
    
    return data.data;
  },

  // Get single discussion
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.DISCUSSIONS}/${id}`);
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to fetch discussion');
    }
    
    return data.data;
  },

  // Create discussion
  create: async (name, description) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.DISCUSSIONS}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, description }),
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to create discussion');
    }
    
    return data.data;
  },

  // Update discussion
  update: async (id, name, description) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.DISCUSSIONS}/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, description }),
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to update discussion');
    }
    
    return data.data;
  },

  // Delete discussion
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.DISCUSSIONS}/${id}`, {
      method: 'DELETE',
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to delete discussion');
    }
    
    return true;
  },
};

