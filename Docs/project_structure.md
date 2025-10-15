# Project Structure

## Root Directory

```
topic-summarizer-mvp/
├── frontend/                    # React + Vite application
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── backend/                     # Flask API server
│   ├── app/
│   ├── requirements.txt
│   ├── .env
│   └── run.py
├── database/                    # SQLite database and migrations
│   ├── instance/
│   └── migrations/
├── uploads/                     # File storage directory
├── Docs/                        # Project documentation
├── tests/                       # Test files
├── .gitignore
├── README.md
└── docker-compose.yml           # Optional: for containerization
```

## Detailed Structure

### Frontend Structure (React + Vite)

```
frontend/
├── public/
│   ├── vite.svg
│   └── favicon.ico
├── src/
│   ├── components/              # Reusable UI components
│   │   ├── common/             # Generic components
│   │   │   ├── Button/
│   │   │   │   ├── Button.jsx
│   │   │   │   └── Button.css
│   │   │   ├── Modal/
│   │   │   │   ├── Modal.jsx
│   │   │   │   └── Modal.css
│   │   │   ├── LoadingSpinner/
│   │   │   │   ├── LoadingSpinner.jsx
│   │   │   │   └── LoadingSpinner.css
│   │   │   └── ErrorMessage/
│   │   │       ├── ErrorMessage.jsx
│   │   │       └── ErrorMessage.css
│   │   ├── discussion/         # Discussion-specific components
│   │   │   ├── DiscussionList/
│   │   │   │   ├── DiscussionList.jsx
│   │   │   │   └── DiscussionList.css
│   │   │   ├── DiscussionCard/
│   │   │   │   ├── DiscussionCard.jsx
│   │   │   │   └── DiscussionCard.css
│   │   │   ├── DiscussionForm/
│   │   │   │   ├── DiscussionForm.jsx
│   │   │   │   └── DiscussionForm.css
│   │   │   └── DiscussionDetail/
│   │   │       ├── DiscussionDetail.jsx
│   │   │       └── DiscussionDetail.css
│   │   ├── file/               # File upload components
│   │   │   ├── FileUpload/
│   │   │   │   ├── FileUpload.jsx
│   │   │   │   └── FileUpload.css
│   │   │   ├── FileList/
│   │   │   │   ├── FileList.jsx
│   │   │   │   └── FileList.css
│   │   │   └── FileStatus/
│   │   │       ├── FileStatus.jsx
│   │   │       └── FileStatus.css
│   │   └── chat/               # Chat interface components
│   │       ├── ChatInterface/
│   │       │   ├── ChatInterface.jsx
│   │       │   └── ChatInterface.css
│   │       ├── MessageList/
│   │       │   ├── MessageList.jsx
│   │       │   └── MessageList.css
│   │       ├── MessageInput/
│   │       │   ├── MessageInput.jsx
│   │       │   └── MessageInput.css
│   │       └── MessageBubble/
│   │           ├── MessageBubble.jsx
│   │           └── MessageBubble.css
│   │   └── topic/              # NEW: Topic discovery components
│   │       ├── TopicDirectory/
│   │       │   ├── TopicDirectory.jsx
│   │       │   └── TopicDirectory.css
│   │       ├── TopicCard/
│   │       │   ├── TopicCard.jsx
│   │       │   └── TopicCard.css
│   │       ├── TopicList/
│   │       │   ├── TopicList.jsx
│   │       │   └── TopicList.css
│   │       ├── TopicMetadata/
│   │       │   ├── TopicMetadata.jsx
│   │       │   └── TopicMetadata.css
│   │       └── GroupByFileToggle/
│   │           ├── GroupByFileToggle.jsx
│   │           └── GroupByFileToggle.css
│   ├── pages/                  # Main application pages
│   │   ├── HomePage/
│   │   │   ├── HomePage.jsx
│   │   │   └── HomePage.css
│   │   ├── DiscussionPage/
│   │   │   ├── DiscussionPage.jsx
│   │   │   └── DiscussionPage.css
│   │   └── NotFoundPage/
│   │       ├── NotFoundPage.jsx
│   │       └── NotFoundPage.css
│   ├── services/               # API and utility services
│   │   ├── api/
│   │   │   ├── discussions.js
│   │   │   ├── files.js
│   │   │   ├── chat.js
│   │   │   ├── topics.js              # NEW: Topic discovery API
│   │   │   └── index.js
│   │   ├── utils/
│   │   │   ├── constants.js
│   │   │   ├── helpers.js
│   │   │   └── validation.js
│   │   └── hooks/
│   │       ├── useApi.js
│   │       ├── useLocalStorage.js
│   │       └── useDebounce.js
│   ├── context/                # React Context providers
│   │   ├── AppContext.jsx
│   │   └── ChatContext.jsx
│   ├── styles/                 # Global styles and themes
│   │   ├── globals.css
│   │   ├── variables.css
│   │   └── components.css
│   ├── assets/                 # Static assets
│   │   ├── images/
│   │   ├── icons/
│   │   └── fonts/
│   ├── App.jsx
│   ├── App.css
│   ├── main.jsx
│   └── index.css
├── package.json
├── vite.config.js
├── tailwind.config.js          # If using Tailwind CSS
└── index.html
```

### Backend Structure (Flask)

```
backend/
├── app/
│   ├── __init__.py
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── discussion.py
│   │   ├── file.py
│   │   ├── file_chunk.py
│   │   └── topic.py               # NEW: Topic model
│   ├── routes/                  # API route handlers
│   │   ├── __init__.py
│   │   ├── discussions.py
│   │   ├── files.py
│   │   ├── chat.py
│   │   └── topics.py              # NEW: Topic discovery endpoints
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── file_processor.py
│   │   ├── gemini_service.py
│   │   ├── database_service.py
│   │   ├── embedding_service.py      # NEW: Text embedding generation
│   │   ├── clustering_service.py     # NEW: Topic clustering logic
│   │   └── topic_labeling_service.py # NEW: LLM topic labeling
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   ├── file_handlers.py
│   │   └── response_helpers.py
│   ├── config/                 # Configuration files
│   │   ├── __init__.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   └── static/                 # Static files (if needed)
├── database/
│   ├── instance/
│   │   └── app.db              # SQLite database file
│   └── migrations/             # Database migration files
│       ├── versions/
│       └── alembic.ini
├── uploads/                    # File upload directory
│   └── discussions/            # Organized by discussion ID
├── logs/                       # Application logs
│   ├── app.log
│   └── error.log
├── tests/                      # Backend tests
│   ├── __init__.py
│   ├── test_discussions.py
│   ├── test_files.py
│   └── test_chat.py
├── requirements.txt           # Updated with topic discovery dependencies
├── .env                        # Environment variables
├── .env.example               # Environment template
├── run.py                     # Application entry point
├── wsgi.py                    # WSGI entry point
└── README.md
```

### Database Structure

```
database/
├── instance/
│   └── app.db                  # SQLite database file
├── migrations/
│   ├── versions/               # Alembic migration files
│   │   ├── 001_initial_migration.py
│   │   ├── 002_add_file_chunks.py
│   │   └── 003_add_indexes.py
│   ├── alembic.ini
│   └── env.py
└── schema.sql                  # Database schema backup
```

### Documentation Structure

```
Docs/
├── Implementation.md           # Main implementation plan
├── project_structure.md       # This file
├── UI_UX_doc.md              # Design system documentation
├── API_documentation.md       # API endpoint documentation
├── deployment_guide.md        # Deployment instructions
└── testing_guide.md          # Testing procedures
```

### Test Structure

```
tests/
├── frontend/                  # Frontend tests
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── utils/
├── backend/                   # Backend tests
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── integration/               # Integration tests
│   ├── test_file_upload_flow.py
│   ├── test_chat_integration.py
│   └── test_end_to_end.py
└── fixtures/                  # Test data
    ├── sample_documents/
    └── test_data.json
```

## File Naming Conventions

### Frontend (React)
- **Components**: PascalCase (e.g., `DiscussionList.jsx`)
- **CSS Files**: Same as component name (e.g., `DiscussionList.css`)
- **Hooks**: camelCase starting with 'use' (e.g., `useApi.js`)
- **Services**: camelCase (e.g., `discussionService.js`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `API_ENDPOINTS.js`)

### Backend (Python)
- **Modules**: snake_case (e.g., `discussion_service.py`)
- **Classes**: PascalCase (e.g., `DiscussionModel`)
- **Functions**: snake_case (e.g., `get_discussion_by_id`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_FILE_SIZE`)

### Database
- **Tables**: PascalCase (e.g., `Discussions`, `FileChunks`)
- **Columns**: snake_case (e.g., `created_at`, `file_path`)
- **Indexes**: `idx_` prefix (e.g., `idx_discussion_id`)

## Configuration Files

### Frontend Configuration
- `package.json`: Dependencies and scripts
- `vite.config.js`: Build configuration
- `tailwind.config.js`: Styling configuration (if using Tailwind)

### Backend Configuration
- `requirements.txt`: Python dependencies
- `.env`: Environment variables
- `config/`: Environment-specific configurations

### Database Configuration
- `alembic.ini`: Migration configuration
- `database/schema.sql`: Schema backup

## Asset Organization

### Frontend Assets
```
src/assets/
├── images/
│   ├── logos/
│   ├── icons/
│   └── backgrounds/
├── fonts/
│   ├── montserrat/
│   └── material-icons/
└── data/
    └── sample-files/
```

### Backend Assets
```
backend/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                  # If using server-side rendering
    └── emails/
```

## Environment-Specific Configurations

### Development
- React dev server: `http://localhost:3000`
- Flask API: `http://localhost:5000`
- SQLite: `database/instance/app.db`
- Logging: Console output

### Production
- Static files: Served from `dist/` directory
- Flask: WSGI server (Gunicorn)
- SQLite: Production database path
- Logging: File-based logging

## Build and Deployment Structure

### Frontend Build
```
dist/                          # Vite build output
├── assets/
│   ├── index-[hash].js
│   ├── index-[hash].css
│   └── [other assets]
├── index.html
└── vite.svg
```

### Backend Deployment
```
deployment/
├── docker/
│   ├── Dockerfile.frontend
│   ├── Dockerfile.backend
│   └── docker-compose.yml
├── scripts/
│   ├── setup.sh
│   ├── deploy.sh
│   └── backup.sh
└── nginx/
    └── nginx.conf
```

## Security Considerations

### File Storage
- Upload directory: Restricted access
- File validation: Server-side only
- File size limits: Enforced at multiple levels

### API Security
- CORS configuration: Restricted origins
- Input validation: All endpoints
- Error handling: No sensitive data exposure

### Database Security
- SQLite file permissions: Restricted access
- Backup encryption: For production data
- Migration security: Version control

## NEW: Topic Discovery Dependencies

### Backend Dependencies (requirements.txt additions)

```
# Topic Discovery Dependencies
sentence-transformers>=2.2.2
bertopic>=0.15.0
scikit-learn>=1.3.0
hdbscan>=0.8.33
numpy>=1.24.0
umap-learn>=0.5.3
```

### Frontend Dependencies (package.json additions)

```json
{
  "dependencies": {
    "react-router-dom": "^6.8.0",
    "axios": "^1.3.0"
  }
}
```

### Database Schema Extensions

```sql
-- Add to existing FileChunks table
ALTER TABLE FileChunks ADD COLUMN embedding BLOB;
ALTER TABLE FileChunks ADD COLUMN cluster_id INTEGER;

-- New Topics table
CREATE TABLE Topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discussion_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    keyphrases TEXT,
    synonyms TEXT,
    frequency INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (discussion_id) REFERENCES Discussions(id) ON DELETE CASCADE
);
```

This structure provides a scalable, maintainable foundation for the Topic-Based Summarizer MVP with advanced topic discovery capabilities while following best practices for both React and Flask development.
