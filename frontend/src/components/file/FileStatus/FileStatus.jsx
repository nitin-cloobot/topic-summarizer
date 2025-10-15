import './FileStatus.css';

const FileStatus = ({ uploaded, errors }) => {
  if (!uploaded && !errors) return null;

  return (
    <div className="file-status">
      {uploaded && uploaded.length > 0 && (
        <div className="file-status__success">
          <span className="material-symbols-outlined">check_circle</span>
          <span>Successfully uploaded {uploaded.length} file(s)</span>
        </div>
      )}
      {errors && errors.length > 0 && (
        <div className="file-status__errors">
          <div className="file-status__error-header">
            <span className="material-symbols-outlined">error</span>
            <span>Failed to upload {errors.length} file(s)</span>
          </div>
          <ul className="file-status__error-list">
            {errors.map((error, index) => (
              <li key={index}>
                <strong>{error.filename}:</strong> {error.error}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default FileStatus;

