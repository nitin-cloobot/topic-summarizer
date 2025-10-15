# Product Requirements Document (PRD)

## 1. Document Overview

| Field | Value |
| :--- | :--- |
| **Product Name** | Topic-Based Summarizer MVP (Set 1: Raw Content) |
| **Document Version** | 1.0 |
| **Date** | October 15, 2025 |
| **Status** | Approved for Development |
| **Target Audience** | Engineering, QA, Product Management |

---

## 2. Goals and Objectives

The primary objective of this initial set is to establish a **stable, locally deployable foundation** for managing discussions, uploading documents, and integrating a preliminary **AI Chat** interface using raw content.

### A. Goals

* **Validate Core Data Flow:** Successfully store and retrieve structured discussion data and unstructured document content (chunks) in SQLite.
* **Establish Key Interfaces:** Implement a functional React UI for discussion management and file uploads.
* **Demonstrate Basic AI Chat:** Provide a testable AI Chat experience, even if it uses a simple raw-content context.

### B. Success Metrics

* 100% of CRUD operations (Create, Read, Update, Delete) on Discussions function correctly.
* File upload and chunking process is stable for up to **30 files** per discussion.
* AI Chat returns a response based on the entire raw content of the associated documents.

---

## 3. Scope and Architectural Overview

### A. Out of Scope (Future Work)

The following items are **strictly excluded** from this MVP:

* User Authentication/Login (User Management)
* **RAG (Retrieval-Augmented Generation) pipeline** and **Pinecone integration**.
* Any Cloud Deployment (AWS, Azure, etc.)
* Support for image files or file types other than PDF/DOCX.
* Advanced summarization features.

### B. Technical Architecture

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend UI** | **React** | Web-based interface for user interaction (Discussions, Uploads, Chat). |
| **Backend API** | **Python (Flask)** | RESTful API to handle business logic, file processing, and LLM interaction. |
| **Database** | **SQLite** | Local, file-based persistence for all data (Discussions, Files, Chunks). |
| **Deployment** | Local Execution | The application runs entirely on the user's machine (Frontend & Backend). |

---

## 4. Functional Requirements

### FR 1. Discussion Management

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 1.1** | Discussion Creation | Users must be able to create a new discussion with a mandatory **Name** and an optional **Description**. |
| **FR 1.2** | Discussion Retrieval | Users must be able to view a list of all existing discussions. |
| **FR 1.3** | Discussion Update | Users must be able to edit the **Name** and/or **Description** of an existing discussion. |
| **FR 1.4** | Discussion Deletion | Users must be able to delete an existing discussion, which must also cascade-delete all associated files and chunks. |

### FR 2. File Upload and Storage

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 2.1** | File Type Validation | The system must only accept **PDF** and **DOCX** files and reject all others (e.g., images). |
| **FR 2.2** | File Quantity Limit | Users can upload a maximum of **30 files** per single discussion. |
| **FR 2.3** | File Processing | Upon upload, files must be parsed, their content extracted, and then divided into **text chunks**. |
| **FR 2.4** | Chunk Storage | All extracted chunks must be stored persistently in the **SQLite `FileChunks` table**. |

### FR 3. AI Chat Interface (Raw Content)

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 3.1** | Dedicated Interface | Each discussion must have a dedicated chat window accessible via the main discussion view. |
| **FR 3.2** | Context Retrieval | When a query is made, the backend must retrieve **ALL** chunks for that discussion to form the context. |
| **FR 3.3** | Raw-Text Based Response | The LLM response must be based *only* on the raw text provided in the prompt context. |
| **FR 3.4** | Test Constraint | For testing, the chat functionality will be verified using a discussion containing a maximum of **2 small files**. |

---

## 5. User Experience Requirements

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **UX 1.1** | No Authentication | The application must bypass any login screen, routing the user directly to the Discussion List View. |
| **UX 1.2** | Clear Feedback | Users must receive clear success/error messages for creating/editing/deleting discussions and for file uploads (e.g., file limit reached, invalid file type). |
| **UX 1.3** | File Status | The Discussion Interface must display a list of successfully uploaded files. |

---

## 6. Data Model Requirements

| Table | Relationship | Key Requirement |
| :--- | :--- | :--- |
| `Discussions` | Independent | Stores name, description, and timestamp. |
| `Files` | $1:N$ with `Discussions` | Stores original filename and links to the parent discussion. |
| `FileChunks` | $1:N$ with `Files` | Stores the raw text content of the chunk and its index/order. |

---

## 7. Testing Requirements (QA)

| Test Case | Description | Expected Outcome |
| :--- | :--- | :--- |
| **TC 1.1** | Discussion CRUD | A discussion is successfully created, edited (name/description), and deleted without error. |
| **TC 2.1** | File Upload Limit | Attempting to upload the **31st file** to a discussion results in an error message. |
| **TC 2.2** | Format Validation | Uploading a `.jpg` or `.txt` file results in a clear rejection message. |
| **TC 3.1** | AI Chat Test | Upload **2 small documents** (PDF and DOCX). Ask a question answerable by the documents. The AI provides a relevant, raw-text based answer. |
| **TC 3.2** | Data Persistence | After uploading files and restarting the local application, the files and their chunks remain accessible in the respective discussion. |