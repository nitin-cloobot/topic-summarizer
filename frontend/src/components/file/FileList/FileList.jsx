import LoadingSpinner from '../../common/LoadingSpinner/LoadingSpinner';
import './FileList.css';

const FileList = ({ files, isLoading }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const formatSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
  };

  if (isLoading) {
    return <LoadingSpinner message="Loading files..." />;
  }

  if (files.length === 0) {
    return (
      <div className="file-list-empty">
        <span className="material-symbols-outlined">description</span>
        <p>No files uploaded yet</p>
      </div>
    );
  }

  return (
    <div className="file-list">
      <h4 className="file-list__title">Uploaded Files ({files.length})</h4>
      <div className="file-list__items">
        {files.map((file) => (
          <div key={file.id} className="file-list__item">
            <span className="material-symbols-outlined file-list__icon">description</span>
            <div className="file-list__info">
              <div className="file-list__name">{file.filename}</div>
              <div className="file-list__meta">
                <span>{formatSize(file.file_size)}</span>
                <span>•</span>
                <span>{formatDate(file.uploaded_at)}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FileList;

