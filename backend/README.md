# Backend API - Topic-Based Summarizer

Flask-based REST API for the Topic-Based Summarizer MVP.

## 🏗️ Structure

```
backend/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models/               # Database models
│   │   ├── discussion.py
│   │   ├── file.py
│   │   └── file_chunk.py
│   ├── routes/               # API endpoints
│   │   ├── discussions.py
│   │   ├── files.py
│   │   └── chat.py
│   ├── services/             # Business logic
│   │   ├── database_service.py
│   │   ├── file_processor.py
│   │   └── gemini_service.py
│   └── utils/                # Utilities
│       ├── validators.py
│       └── response_helpers.py
├── database/                 # SQLite database
├── uploads/                  # Uploaded files
├── logs/                     # Application logs
├── requirements.txt          # Python dependencies
├── logging_config.py         # Logging configuration
└── run.py                    # Application entry point
```

## 🚀 Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file (see `.env.example`)

5. Run the server:
```bash
python run.py
```

## 📝 API Endpoints

### Health Check
```
GET /api/health
```

### Discussions
```
GET    /api/discussions          # List all
POST   /api/discussions          # Create new
GET    /api/discussions/:id      # Get one
PUT    /api/discussions/:id      # Update
DELETE /api/discussions/:id      # Delete
```

### Files
```
GET  /api/discussions/:id/files  # List files
POST /api/discussions/:id/files  # Upload files
```

### Chat
```
POST /api/discussions/:id/chat   # Send message
```

## 🗄️ Database Schema

### Discussions
- id (INTEGER, PRIMARY KEY)
- name (TEXT, NOT NULL)
- description (TEXT)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### Files
- id (INTEGER, PRIMARY KEY)
- discussion_id (INTEGER, FOREIGN KEY)
- filename (TEXT, NOT NULL)
- file_path (TEXT, NOT NULL)
- file_size (INTEGER)
- uploaded_at (TIMESTAMP)

### FileChunks
- id (INTEGER, PRIMARY KEY)
- file_id (INTEGER, FOREIGN KEY)
- chunk_index (INTEGER)
- content (TEXT, NOT NULL)
- created_at (TIMESTAMP)

## 🔧 Configuration

Environment variables in `.env`:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_PATH=database/instance/app.db
UPLOAD_FOLDER=uploads
MAX_FILE_SIZE=52428800
MAX_FILES_PER_DISCUSSION=30
LLM_API_KEY=your-gemini-api-key
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
LOG_LEVEL=INFO
```

## 📚 Dependencies

- Flask 3.0.0 - Web framework
- Flask-CORS 4.0.0 - CORS support
- PyPDF2 3.0.1 - PDF processing
- python-docx 1.1.0 - DOCX processing
- requests 2.31.0 - HTTP client
- python-dotenv 1.0.0 - Environment management

## 🔍 Logging

Logs are stored in the `logs/` directory:
- `app.log` - General application logs
- `error.log` - Error and exception logs

## 🧪 Testing

Run tests:
```bash
python -m pytest tests/
```

## 🛠️ Development

1. Make changes to code
2. Test locally
3. Check logs for errors
4. Update documentation if needed

