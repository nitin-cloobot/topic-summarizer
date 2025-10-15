import os
import PyPDF2
import docx
from logging_config import app_logger, error_logger

class FileProcessor:
    """Service for processing and chunking files"""
    
    CHUNK_SIZE = 1000  # Characters per chunk
    CHUNK_OVERLAP = 200  # Overlap between chunks for context
    
    @staticmethod
    def extract_text_from_pdf(file_path):
        """Extract text from PDF file"""
        try:
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            app_logger.info(f"Extracted {len(text)} characters from PDF: {file_path}")
            return text
        except Exception as e:
            error_logger.error(f"Error extracting text from PDF {file_path}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def extract_text_from_docx(file_path):
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            app_logger.info(f"Extracted {len(text)} characters from DOCX: {file_path}")
            return text
        except Exception as e:
            error_logger.error(f"Error extracting text from DOCX {file_path}: {e}", exc_info=True)
            raise
    
    @staticmethod
    def extract_text(file_path):
        """Extract text from file based on extension"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        if ext == '.pdf':
            return FileProcessor.extract_text_from_pdf(file_path)
        elif ext in ['.docx', '.doc']:
            return FileProcessor.extract_text_from_docx(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    
    @staticmethod
    def chunk_text(text, chunk_size=None, chunk_overlap=None):
        """Split text into overlapping chunks"""
        if chunk_size is None:
            chunk_size = FileProcessor.CHUNK_SIZE
        if chunk_overlap is None:
            chunk_overlap = FileProcessor.CHUNK_OVERLAP
        
        if not text or len(text) == 0:
            return []
        
        chunks = []
        start = 0
        text_length = len(text)
        
        while start < text_length:
            end = start + chunk_size
            
            # If this is not the last chunk, try to break at a sentence or word boundary
            if end < text_length:
                # Look for sentence boundary (., !, ?)
                for i in range(end, max(start, end - 100), -1):
                    if text[i] in '.!?\n':
                        end = i + 1
                        break
                else:
                    # If no sentence boundary, look for word boundary
                    for i in range(end, max(start, end - 50), -1):
                        if text[i].isspace():
                            end = i
                            break
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Move start position with overlap
            start = end - chunk_overlap if end < text_length else text_length
        
        app_logger.info(f"Created {len(chunks)} chunks from text of length {text_length}")
        return chunks
    
    @staticmethod
    def process_file(file_path):
        """Extract text and create chunks from a file"""
        try:
            # Extract text
            text = FileProcessor.extract_text(file_path)
            
            # Create chunks
            chunks = FileProcessor.chunk_text(text)
            
            app_logger.info(f"Processed file {file_path}: {len(chunks)} chunks created")
            return chunks
        except Exception as e:
            error_logger.error(f"Error processing file {file_path}: {e}", exc_info=True)
            raise

