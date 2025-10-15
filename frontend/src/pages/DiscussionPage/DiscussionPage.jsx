import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '../../components/common/Button/Button';
import Modal from '../../components/common/Modal/Modal';
import DiscussionDetail from '../../components/discussion/DiscussionDetail/DiscussionDetail';
import DiscussionForm from '../../components/discussion/DiscussionForm/DiscussionForm';
import FileUpload from '../../components/file/FileUpload/FileUpload';
import FileList from '../../components/file/FileList/FileList';
import FileStatus from '../../components/file/FileStatus/FileStatus';
import ChatInterface from '../../components/chat/ChatInterface/ChatInterface';
import LoadingSpinner from '../../components/common/LoadingSpinner/LoadingSpinner';
import ErrorMessage from '../../components/common/ErrorMessage/ErrorMessage';
import { discussionService, fileService } from '../../services/api';
import './DiscussionPage.css';

const DiscussionPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  
  const [discussion, setDiscussion] = useState(null);
  const [files, setFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isFilesLoading, setIsFilesLoading] = useState(false);
  const [error, setError] = useState('');
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState(null);

  useEffect(() => {
    fetchDiscussion();
    fetchFiles();
  }, [id]);

  const fetchDiscussion = async () => {
    try {
      setIsLoading(true);
      setError('');
      const data = await discussionService.getById(id);
      setDiscussion(data);
    } catch (err) {
      setError(err.message || 'Failed to load discussion');
    } finally {
      setIsLoading(false);
    }
  };

  const fetchFiles = async () => {
    try {
      setIsFilesLoading(true);
      const data = await fileService.getByDiscussion(id);
      setFiles(data);
    } catch (err) {
      console.error('Failed to load files:', err);
    } finally {
      setIsFilesLoading(false);
    }
  };

  const handleEditDiscussion = async (formData) => {
    try {
      setIsSubmitting(true);
      setError('');
      await discussionService.update(id, formData.name, formData.description);
      await fetchDiscussion();
      setIsEditModalOpen(false);
    } catch (err) {
      setError(err.message || 'Failed to update discussion');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleFileUpload = async (selectedFiles) => {
    try {
      setIsUploading(true);
      setError('');
      setUploadStatus(null);
      
      const result = await fileService.upload(id, selectedFiles);
      
      setUploadStatus({
        uploaded: result.uploaded,
        errors: result.errors
      });
      
      await fetchFiles();
    } catch (err) {
      setError(err.message || 'Failed to upload files');
    } finally {
      setIsUploading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="discussion-page">
        <div className="container">
          <LoadingSpinner message="Loading discussion..." />
        </div>
      </div>
    );
  }

  if (error && !discussion) {
    return (
      <div className="discussion-page">
        <div className="container">
          <ErrorMessage message={error} />
          <Button onClick={() => navigate('/')}>Back to Home</Button>
        </div>
      </div>
    );
  }

  return (
    <div className="discussion-page">
      <div className="container">
        <div className="discussion-page__nav">
          <Button
            variant="secondary"
            icon="arrow_back"
            onClick={() => navigate('/')}
          >
            Back to Discussions
          </Button>
        </div>

        {error && <ErrorMessage message={error} onDismiss={() => setError('')} />}

        <DiscussionDetail
          discussion={discussion}
          onEdit={() => setIsEditModalOpen(true)}
        />

        <div className="discussion-page__grid">
          <div className="discussion-page__files">
            <h2>Files & Upload</h2>
            
            <FileUpload
              onUpload={handleFileUpload}
              isUploading={isUploading}
              currentFileCount={files.length}
            />

            {uploadStatus && (
              <FileStatus
                uploaded={uploadStatus.uploaded}
                errors={uploadStatus.errors}
              />
            )}

            <FileList files={files} isLoading={isFilesLoading} />
          </div>

          <div className="discussion-page__chat">
            <ChatInterface discussionId={id} filesCount={files.length} />
          </div>
        </div>

        {/* Edit Discussion Modal */}
        <Modal
          isOpen={isEditModalOpen}
          onClose={() => setIsEditModalOpen(false)}
          title="Edit Discussion"
        >
          <DiscussionForm
            onSubmit={handleEditDiscussion}
            initialData={discussion}
            isLoading={isSubmitting}
          />
        </Modal>
      </div>
    </div>
  );
};

export default DiscussionPage;

