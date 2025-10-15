export const API_BASE_URL = '/api';

export const API_ENDPOINTS = {
  DISCUSSIONS: '/discussions',
  FILES: (discussionId) => `/discussions/${discussionId}/files`,
  CHAT: (discussionId) => `/discussions/${discussionId}/chat`,
};

export const FILE_CONSTRAINTS = {
  MAX_FILES: 30,
  MAX_FILE_SIZE: 50 * 1024 * 1024, // 50MB
  ALLOWED_TYPES: ['.pdf', '.docx', '.doc'],
  ALLOWED_MIME_TYPES: [
    'application/pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/msword'
  ]
};

