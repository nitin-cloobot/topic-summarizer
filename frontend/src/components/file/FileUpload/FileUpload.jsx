import { useState, useRef } from 'react';
import Button from '../../common/Button/Button';
import ErrorMessage from '../../common/ErrorMessage/ErrorMessage';
import { FILE_CONSTRAINTS } from '../../../services/utils/constants';
import './FileUpload.css';

const FileUpload = ({ onUpload, isUploading = false, currentFileCount = 0 }) => {
  const [dragActive, setDragActive] = useState(false);
  const [error, setError] = useState('');
  const [selectedFiles, setSelectedFiles] = useState([]);
  const fileInputRef = useRef(null);

  const validateFiles = (files) => {
    const fileArray = Array.from(files);
    const errors = [];

    // Check file count
    if (currentFileCount + fileArray.length > FILE_CONSTRAINTS.MAX_FILES) {
      errors.push(`Maximum ${FILE_CONSTRAINTS.MAX_FILES} files allowed per discussion`);
    }

    // Check file types and sizes
    fileArray.forEach(file => {
      const extension = '.' + file.name.split('.').pop().toLowerCase();
      
      if (!FILE_CONSTRAINTS.ALLOWED_TYPES.includes(extension)) {
        errors.push(`${file.name}: Invalid file type. Only PDF and DOCX files are allowed.`);
      }
      
      if (file.size > FILE_CONSTRAINTS.MAX_FILE_SIZE) {
        errors.push(`${file.name}: File size exceeds 50MB limit.`);
      }
    });

    return errors;
  };

  const handleFiles = (files) => {
    setError('');
    
    const validationErrors = validateFiles(files);
    if (validationErrors.length > 0) {
      setError(validationErrors.join(' '));
      return;
    }

    setSelectedFiles(Array.from(files));
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFiles(e.dataTransfer.files);
    }
  };

  const handleChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      handleFiles(e.target.files);
    }
  };

  const handleUploadClick = () => {
    if (selectedFiles.length > 0) {
      onUpload(selectedFiles);
      setSelectedFiles([]);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    }
  };

  const handleRemoveFile = (index) => {
    setSelectedFiles(selectedFiles.filter((_, i) => i !== index));
  };

  return (
    <div className="file-upload">
      {error && <ErrorMessage message={error} onDismiss={() => setError('')} />}
      
      <div
        className={`file-upload__dropzone ${dragActive ? 'file-upload__dropzone--active' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
      >
        <span className="material-symbols-outlined file-upload__icon">cloud_upload</span>
        <h4>Drag & Drop Files Here</h4>
        <p>or click to browse</p>
        <p className="file-upload__hint">
          Supports PDF and DOCX files (max {FILE_CONSTRAINTS.MAX_FILES} files, 50MB each)
        </p>
        <input
          ref={fileInputRef}
          type="file"
          multiple
          accept=".pdf,.docx,.doc"
          onChange={handleChange}
          className="file-upload__input"
        />
      </div>

      {selectedFiles.length > 0 && (
        <div className="file-upload__selected">
          <h4>Selected Files ({selectedFiles.length})</h4>
          <div className="file-upload__list">
            {selectedFiles.map((file, index) => (
              <div key={index} className="file-upload__item">
                <span className="material-symbols-outlined">description</span>
                <span className="file-upload__name">{file.name}</span>
                <span className="file-upload__size">
                  {(file.size / 1024 / 1024).toFixed(2)} MB
                </span>
                <button
                  className="file-upload__remove"
                  onClick={() => handleRemoveFile(index)}
                  disabled={isUploading}
                >
                  <span className="material-symbols-outlined">close</span>
                </button>
              </div>
            ))}
          </div>
          <Button
            variant="primary"
            fullWidth
            onClick={handleUploadClick}
            disabled={isUploading}
          >
            {isUploading ? 'Uploading...' : `Upload ${selectedFiles.length} File(s)`}
          </Button>
        </div>
      )}
    </div>
  );
};

export default FileUpload;

