# Topic-Based Summarizer MVP

A full-stack application for managing discussions, uploading documents (PDF/DOCX), and chatting with AI to understand document content using Google Gemini 2.5 Flash API.

## 📋 Overview

This MVP allows users to:
- Create and manage discussions
- Upload PDF and DOCX files (up to 30 per discussion)
- Chat with AI about the uploaded document content
- Get AI-powered responses based on document context

## 🏗️ Architecture

- **Frontend**: React 18 + Vite (Latest)
- **Backend**: Python Flask 3.x
- **Database**: SQLite
- **AI**: Google Gemini 2.5 Flash API
- **Design**: Material Design 3 Dark Mode

## 📁 Project Structure

```
oct-15/
├── frontend/          # React + Vite application
├── backend/           # Flask API server
├── Docs/             # Project documentation
├── gemini_flash.py   # Reference Gemini implementation
└── PRD.md            # Product Requirements Document
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ (for frontend)
- **Python** 3.9+ (for backend)
- **Google Gemini API Key** ([Get one here](https://ai.google.dev/))

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the backend directory:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_PATH=database/instance/app.db
UPLOAD_FOLDER=uploads
MAX_FILE_SIZE=52428800
MAX_FILES_PER_DISCUSSION=30
LLM_API_KEY=your-gemini-api-key-here
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
LOG_LEVEL=INFO
```

6. Run the Flask server:
```bash
python run.py
```

The backend API will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 🎨 Design System

The application follows **Google Material Design 3** with a dark theme:

### Color Palette
- **Background**: #0D0D0D (darkest) to #4D4D4D (lightest surface)
- **Accent**: Magenta (#C82FFF) and Blue (#00AAFF)
- **Text**: White (#FFFFFF) and Gray (#A8A8A8)
- **Gradient**: Magenta to Blue for primary CTAs

### Typography
- **Font**: Montserrat (Regular, Medium, Semi-Bold)
- **Icons**: Material Symbols (Weight 200, Outlined)

## 📚 API Endpoints

### Discussions
- `GET /api/discussions` - List all discussions
- `POST /api/discussions` - Create new discussion
- `GET /api/discussions/:id` - Get specific discussion
- `PUT /api/discussions/:id` - Update discussion
- `DELETE /api/discussions/:id` - Delete discussion

### Files
- `GET /api/discussions/:id/files` - List files in discussion
- `POST /api/discussions/:id/files` - Upload files to discussion

### Chat
- `POST /api/discussions/:id/chat` - Send message to AI

## 🧪 Testing

### Test Cases

**TC 1.1 - Discussion CRUD**
- Create a discussion with name and description
- Edit the discussion details
- Delete the discussion
- Verify cascade deletion of files

**TC 2.1 - File Upload Limit**
- Upload 30 files successfully
- Attempt to upload the 31st file
- Verify error message

**TC 2.2 - File Type Validation**
- Upload a PDF file (success)
- Upload a DOCX file (success)
- Upload a JPG file (rejection)
- Verify error messages

**TC 3.1 - AI Chat**
- Upload 2 small PDF/DOCX files
- Ask a question answerable by the documents
- Verify AI provides relevant response

**TC 3.2 - Data Persistence**
- Upload files
- Restart the application
- Verify files and chunks are still accessible

## 📝 Features

### Must-Have (Implemented)
✅ Discussion CRUD operations  
✅ File upload with PDF/DOCX validation  
✅ File chunking and storage  
✅ AI Chat interface with Gemini integration  
✅ SQLite data persistence  
✅ Responsive React UI  

### Future Enhancements
⏳ User authentication  
⏳ RAG (Retrieval-Augmented Generation)  
⏳ Pinecone integration for vector search  
⏳ Cloud deployment  
⏳ Image file support  
⏳ Advanced summarization features  

## 🔧 Development

### Backend Development
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python run.py
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Build for Production
```bash
cd frontend
npm run build
```

## 📖 Documentation

For detailed documentation, see the `Docs/` folder:
- **Implementation.md** - Implementation plan and tech stack
- **project_structure.md** - File organization
- **UI_UX_doc.md** - Design system documentation
- **Bug_Tracking.md** - Issue tracking

## 🐛 Known Issues

See `Docs/Bug_Tracking.md` for current issues and their status.

## 🤝 Contributing

1. Follow the design system guidelines in `Docs/UI_UX_doc.md`
2. Maintain the project structure as defined in `Docs/project_structure.md`
3. Update documentation when adding new features
4. Test thoroughly before committing

## 📄 License

This project is part of a hackathon MVP and is for demonstration purposes.

## 🙏 Acknowledgments

- Google Gemini API for AI capabilities
- Material Design 3 for design system
- React and Flask communities for excellent tooling

---

**Built with ❤️ for the October 15, 2025 Hackathon**

