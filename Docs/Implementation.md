# Implementation Plan for Topic-Based Summarizer MVP

## Feature Analysis

### Identified Features:

1. **Discussion Management System**
   - Create new discussions with name and description
   - View list of all discussions
   - Edit discussion details (name/description)
   - Delete discussions with cascade deletion of files and chunks

2. **File Upload and Processing**
   - Upload PDF and DOCX files only (validation)
   - Maximum 30 files per discussion
   - File content extraction and chunking
   - Persistent storage of file chunks in SQLite

3. **AI Chat Interface**
   - Dedicated chat window per discussion
   - Context retrieval from all discussion chunks
   - Raw-text based AI responses using Gemini 2.5 Flash
   - Integration with existing Gemini API utility

4. **Data Persistence**
   - SQLite database with three main tables
   - Discussions, Files, and FileChunks relationships
   - Local file-based storage

5. **User Interface**
   - No authentication required
   - Discussion list view as entry point
   - File upload interface with status feedback
   - Chat interface for AI interactions

### Feature Categorization:

- **Must-Have Features:** 
  - Discussion CRUD operations
  - File upload with PDF/DOCX validation
  - File chunking and storage
  - AI Chat interface with Gemini integration
  - SQLite data persistence
  - Basic React UI for all operations

- **Should-Have Features:**
  - File upload progress indicators
  - Error handling and user feedback
  - Responsive design
  - File status display in discussions

- **Nice-to-Have Features:**
  - File preview capabilities
  - Chat history persistence
  - Advanced error recovery
  - Performance optimizations

## Recommended Tech Stack

### Frontend:

- **Framework:** React 19 with Vite 6 - Latest stable versions with excellent development experience and build performance
- **Documentation:** [Vite Official Docs](https://vite.dev/), [React 19 Docs](https://react.dev/)

### Backend:

- **Framework:** Python Flask 3.x - Lightweight, flexible, and perfect for REST API development
- **Documentation:** [Flask Official Docs](https://flask.palletsprojects.com/)

### Database:

- **Database:** SQLite 3 - File-based, zero-configuration, perfect for local deployment
- **Documentation:** [SQLite Official Docs](https://www.sqlite.org/docs.html)

### AI Integration:

- **LLM Service:** Google Gemini 2.5 Flash API - Cost-effective, fast, and reliable for text processing
- **Documentation:** [Gemini API Docs](https://ai.google.dev/docs)

### Additional Tools:

- **File Processing:** PyPDF2 and python-docx - Reliable libraries for PDF and DOCX parsing
- **HTTP Client:** Requests - Standard Python library for API calls
- **CORS Handling:** Flask-CORS - Enable cross-origin requests for React-Flask communication
- **Environment Management:** python-dotenv - Secure API key management
- **Documentation:** [PyPDF2 Docs](https://pypdf2.readthedocs.io/), [python-docx Docs](https://python-docx.readthedocs.io/)

## Implementation Stages

### Stage 1: Foundation & Setup

**Duration:** 3-4 days

**Dependencies:** None

#### Sub-steps:

- [ ] Set up development environment (Node.js 18+, Python 3.9+)
- [ ] Initialize React project with Vite and latest template
- [ ] Set up Flask backend project structure
- [ ] Configure SQLite database with three main tables (Discussions, Files, FileChunks)
- [ ] Implement basic Flask CORS configuration
- [ ] Set up environment variables for API keys
- [ ] Create basic project documentation structure

### Stage 2: Core Features

**Duration:** 5-7 days

**Dependencies:** Stage 1 completion

#### Sub-steps:

- [ ] Implement Discussion CRUD API endpoints (Create, Read, Update, Delete)
- [ ] Create React components for Discussion List and Discussion Detail views
- [ ] Implement file upload API with PDF/DOCX validation
- [ ] Develop file processing pipeline (extraction and chunking)
- [ ] Create file upload React component with drag-and-drop support
- [ ] Implement SQLite data persistence for all entities
- [ ] Set up basic routing between discussion list and detail views

### Stage 3: AI Integration & Chat

**Duration:** 4-5 days

**Dependencies:** Stage 2 completion

#### Sub-steps:

- [ ] Integrate existing Gemini 2.5 Flash API utility
- [ ] Create chat API endpoint that retrieves all chunks for a discussion
- [ ] Implement context building from file chunks
- [ ] Develop React chat interface component
- [ ] Add chat history display and message handling
- [ ] Implement error handling for AI API calls
- [ ] Test AI responses with sample documents

### Stage 4: Polish & Optimization

**Duration:** 3-4 days

**Dependencies:** Stage 3 completion

#### Sub-steps:

- [ ] Implement comprehensive error handling and user feedback
- [ ] Add file upload progress indicators and status display
- [ ] Optimize file processing performance for large documents
- [ ] Enhance UI/UX with proper loading states and animations
- [ ] Implement data validation and sanitization
- [ ] Add comprehensive testing for all CRUD operations
- [ ] Prepare local deployment documentation

## Resource Links

- [Vite Official Documentation](https://vite.dev/)
- [React 19 Documentation](https://react.dev/)
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [Flask-CORS Documentation](https://flask-cors.readthedocs.io/)
- [React File Upload Best Practices](https://react.dev/learn/responding-to-events)
- [SQLite Python Integration Guide](https://docs.python.org/3/library/sqlite3.html)

## Technical Architecture Details

### Database Schema

```sql
-- Discussions table
CREATE TABLE Discussions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Files table
CREATE TABLE Files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discussion_id INTEGER NOT NULL,
    filename TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (discussion_id) REFERENCES Discussions(id) ON DELETE CASCADE
);

-- FileChunks table
CREATE TABLE FileChunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES Files(id) ON DELETE CASCADE
);
```

### API Endpoints

```
GET    /api/discussions           # List all discussions
POST   /api/discussions           # Create new discussion
GET    /api/discussions/:id       # Get specific discussion
PUT    /api/discussions/:id       # Update discussion
DELETE /api/discussions/:id       # Delete discussion

POST   /api/discussions/:id/files # Upload files to discussion
GET    /api/discussions/:id/files # List files in discussion

POST   /api/discussions/:id/chat  # Send message to AI chat
```

### File Processing Pipeline

1. **File Upload Validation**
   - Check file type (PDF/DOCX only)
   - Verify file size limits
   - Check discussion file count (max 30)

2. **Content Extraction**
   - PDF: Use PyPDF2 to extract text
   - DOCX: Use python-docx to extract text

3. **Chunking Strategy**
   - Split text into manageable chunks (500-1000 characters)
   - Preserve context boundaries (sentence/paragraph breaks)
   - Store chunks with index for ordering

4. **AI Context Building**
   - Retrieve all chunks for a discussion
   - Combine into context string
   - Send to Gemini API with user query

## Testing Strategy

### Unit Tests
- [ ] Test all CRUD operations for discussions
- [ ] Test file upload validation and processing
- [ ] Test AI API integration and response handling
- [ ] Test database operations and relationships

### Integration Tests
- [ ] Test complete file upload to chat workflow
- [ ] Test AI responses with actual document content
- [ ] Test error handling and edge cases
- [ ] Test data persistence across application restarts

### User Acceptance Tests
- [ ] Create discussion and upload 2 small test files
- [ ] Ask AI questions answerable by the documents
- [ ] Verify AI provides relevant, context-based responses
- [ ] Test file limit enforcement (31st file rejection)
- [ ] Test invalid file type rejection

## Deployment Considerations

### Local Development
- React dev server on port 3000
- Flask API server on port 5000
- SQLite database file in project root
- Environment variables for API keys

### Production Readiness
- Build React app for static serving
- Configure Flask for production WSGI server
- Set up proper logging and error handling
- Implement data backup strategies

## Risk Mitigation

### Technical Risks
- **File Processing Performance**: Implement chunking limits and progress indicators
- **AI API Rate Limits**: Add retry logic and error handling
- **Database Corruption**: Regular backups and transaction management
- **Memory Usage**: Stream large file processing, implement cleanup

### User Experience Risks
- **File Upload Failures**: Clear error messages and retry mechanisms
- **AI Response Quality**: Fallback responses and context validation
- **Data Loss**: Confirmation dialogs for destructive operations
- **Performance Issues**: Loading states and progress indicators
