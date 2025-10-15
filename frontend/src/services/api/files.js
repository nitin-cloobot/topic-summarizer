import { API_BASE_URL, API_ENDPOINTS } from '../utils/constants';

export const fileService = {
  // Get files for a discussion
  getByDiscussion: async (discussionId) => {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.FILES(discussionId)}`);
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to fetch files');
    }
    
    return data.data;
  },

  // Upload files
  upload: async (discussionId, files) => {
    const formData = new FormData();
    
    for (let i = 0; i < files.length; i++) {
      formData.append('files', files[i]);
    }
    
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.FILES(discussionId)}`, {
      method: 'POST',
      body: formData,
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message || 'Failed to upload files');
    }
    
    return data.data;
  },
};

