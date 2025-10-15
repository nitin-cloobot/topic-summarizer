# Complete Setup Guide - Topic-Based Summarizer MVP

This guide will walk you through setting up and running the Topic-Based Summarizer application.

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
2. **Python** (v3.9 or higher) - [Download](https://www.python.org/)
3. **Google Gemini API Key** - [Get one here](https://ai.google.dev/)

## 🚀 Step-by-Step Setup

### Step 1: Clone/Download the Project

If you haven't already, navigate to the project directory:
```bash
cd C:\Users\nitin\Desktop\Hackathon\oct-15
```

### Step 2: Backend Setup

#### 2.1 Create Virtual Environment

Open a terminal in the project root and run:

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

With the virtual environment activated:
```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- Flask-CORS 4.0.0
- PyPDF2 3.0.1
- python-docx 1.1.0
- requests 2.31.0
- python-dotenv 1.0.0

#### 2.3 Configure Environment Variables

Create a `.env` file in the `backend` directory with the following content:

```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=dev-secret-key-change-in-production

# Database Configuration
DATABASE_PATH=database/instance/app.db

# Upload Configuration
UPLOAD_FOLDER=uploads
MAX_FILE_SIZE=52428800
MAX_FILES_PER_DISCUSSION=30

# LLM Configuration (IMPORTANT: Add your API key here)
LLM_API_KEY=YOUR_GEMINI_API_KEY_HERE

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# Logging Configuration
LOG_LEVEL=INFO
```

**⚠️ IMPORTANT:** Replace `YOUR_GEMINI_API_KEY_HERE` with your actual Gemini API key!

#### 2.4 Start the Backend Server

With the virtual environment still activated:
```bash
python run.py
```

You should see:
```
Starting Flask application on port 5000
Debug mode: True
 * Running on http://0.0.0.0:5000
```

**✅ Backend is now running on http://localhost:5000**

### Step 3: Frontend Setup

Open a **NEW** terminal window (keep the backend running).

#### 3.1 Navigate to Frontend Directory

```bash
cd frontend
```

#### 3.2 Install Node Dependencies

```bash
npm install
```

This will install:
- React 18.3.1
- React Router DOM 6.26.0
- Vite 5.4.2
- Other dev dependencies

#### 3.3 Start the Frontend Development Server

```bash
npm run dev
```

You should see:
```
VITE v5.4.2  ready in XXX ms

➜  Local:   http://localhost:3000/
➜  Network: use --host to expose
```

**✅ Frontend is now running on http://localhost:3000**

## 🧪 Testing the Application

### Test 1: Create a Discussion

1. Open your browser and go to `http://localhost:3000`
2. Click the **"New Discussion"** button
3. Enter:
   - Name: "Test Discussion"
   - Description: "This is a test discussion for the MVP"
4. Click **"Create Discussion"**
5. ✅ You should see the new discussion card appear

### Test 2: Upload Files

1. Click on your newly created discussion
2. You'll see the discussion detail page with two sections: Files & Chat
3. In the **Files & Upload** section:
   - Drag and drop a PDF or DOCX file, OR
   - Click the upload area to browse for files
4. Click **"Upload X File(s)"**
5. ✅ You should see:
   - Success message
   - File listed in the "Uploaded Files" section

### Test 3: Chat with AI

1. After uploading files, go to the **Chat** section
2. Type a question related to your document content
   - Example: "What is the main topic of this document?"
3. Click **"Send"** or press Enter
4. ✅ You should see:
   - Your message appears on the right (gradient background)
   - AI response appears on the left (dark background)
   - Response based on your document content

### Test 4: File Validation

1. Try uploading an unsupported file (e.g., .jpg, .txt)
2. ✅ You should see an error message: "Invalid file type. Only PDF and DOCX files are allowed."

### Test 5: Edit Discussion

1. From the home page, click **"Edit"** on any discussion card
2. Change the name or description
3. Click **"Update Discussion"**
4. ✅ Discussion should update immediately

### Test 6: Delete Discussion

1. From the home page, click **"Delete"** on any discussion card
2. Confirm the deletion in the modal
3. ✅ Discussion should be removed along with all its files

## 📱 Accessing the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Health Check**: http://localhost:5000/api/health

## 🛠️ Troubleshooting

### Backend Issues

**Issue: "No module named 'flask'"**
- Solution: Make sure virtual environment is activated and dependencies are installed
```bash
cd backend
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

**Issue: "LLM_API_KEY not found"**
- Solution: Check that `.env` file exists in `backend/` directory and contains your Gemini API key

**Issue: "Port 5000 already in use"**
- Solution: Either kill the process using port 5000, or change the port in `.env`:
```env
PORT=5001
```

### Frontend Issues

**Issue: "Cannot GET /"**
- Solution: Make sure you're accessing `http://localhost:3000` (not 5000)

**Issue: "Failed to fetch discussions"**
- Solution: Ensure backend is running on port 5000 and CORS is configured correctly

**Issue: "npm: command not found"**
- Solution: Install Node.js from https://nodejs.org/

### File Upload Issues

**Issue: "Failed to upload files"**
- Solution: Check:
  1. File is PDF or DOCX
  2. File size is under 50MB
  3. Backend `uploads/` directory has write permissions

**Issue: "File limit exceeded"**
- Solution: Maximum 30 files per discussion. Delete some files or create a new discussion.

### Chat Issues

**Issue: "Please upload files before starting a chat"**
- Solution: Upload at least one PDF or DOCX file before chatting

**Issue: "AI Error: Unable to generate response"**
- Solution: Check:
  1. Gemini API key is valid in `.env` file
  2. You have internet connection
  3. Check backend logs in `backend/logs/` for more details

## 📊 Monitoring

### Backend Logs

Logs are stored in `backend/logs/`:
- `app.log` - General application logs
- `error.log` - Error logs

View real-time logs:
```bash
# Windows (PowerShell)
Get-Content backend\logs\app.log -Wait

# Mac/Linux
tail -f backend/logs/app.log
```

### Database

SQLite database is located at:
```
backend/database/instance/app.db
```

You can view it with tools like:
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [SQLite Viewer VS Code Extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)

## 🎯 Next Steps

Once everything is working:

1. **Try uploading multiple files** to test the chunking system
2. **Ask complex questions** to test AI understanding
3. **Test on different browsers** (Chrome, Firefox, Edge)
4. **Test responsive design** by resizing the browser window
5. **Review the code** to understand the architecture

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Material Design 3](https://m3.material.io/)

## 🆘 Need Help?

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the logs in `backend/logs/`
3. Check browser console for frontend errors (F12)
4. Verify all prerequisites are installed correctly
5. Ensure `.env` file is configured properly

---

**Happy Testing! 🚀**

