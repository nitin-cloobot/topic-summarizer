import { useState, useEffect } from 'react';
import Button from '../../components/common/Button/Button';
import Modal from '../../components/common/Modal/Modal';
import DiscussionList from '../../components/discussion/DiscussionList/DiscussionList';
import DiscussionForm from '../../components/discussion/DiscussionForm/DiscussionForm';
import ErrorMessage from '../../components/common/ErrorMessage/ErrorMessage';
import { discussionService } from '../../services/api';
import './HomePage.css';

const HomePage = () => {
  const [discussions, setDiscussions] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedDiscussion, setSelectedDiscussion] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    fetchDiscussions();
  }, []);

  const fetchDiscussions = async () => {
    try {
      setIsLoading(true);
      setError('');
      const data = await discussionService.getAll();
      setDiscussions(data);
    } catch (err) {
      setError(err.message || 'Failed to load discussions');
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateDiscussion = async (formData) => {
    try {
      setIsSubmitting(true);
      setError('');
      await discussionService.create(formData.name, formData.description);
      await fetchDiscussions();
      setIsCreateModalOpen(false);
    } catch (err) {
      setError(err.message || 'Failed to create discussion');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleEditDiscussion = async (formData) => {
    try {
      setIsSubmitting(true);
      setError('');
      await discussionService.update(
        selectedDiscussion.id,
        formData.name,
        formData.description
      );
      await fetchDiscussions();
      setIsEditModalOpen(false);
      setSelectedDiscussion(null);
    } catch (err) {
      setError(err.message || 'Failed to update discussion');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleDeleteDiscussion = async () => {
    try {
      setIsSubmitting(true);
      setError('');
      await discussionService.delete(selectedDiscussion.id);
      await fetchDiscussions();
      setIsDeleteModalOpen(false);
      setSelectedDiscussion(null);
    } catch (err) {
      setError(err.message || 'Failed to delete discussion');
    } finally {
      setIsSubmitting(false);
    }
  };

  const openEditModal = (discussion) => {
    setSelectedDiscussion(discussion);
    setIsEditModalOpen(true);
  };

  const openDeleteModal = (discussion) => {
    setSelectedDiscussion(discussion);
    setIsDeleteModalOpen(true);
  };

  return (
    <div className="home-page">
      <div className="container">
        <header className="home-page__header">
          <div>
            <h1>Topic-Based Summarizer</h1>
            <p className="home-page__subtitle">
              Upload documents and chat with AI to understand your content
            </p>
          </div>
          <Button
            variant="primary"
            icon="add"
            onClick={() => setIsCreateModalOpen(true)}
          >
            New Discussion
          </Button>
        </header>

        {error && <ErrorMessage message={error} onDismiss={() => setError('')} />}

        <DiscussionList
          discussions={discussions}
          isLoading={isLoading}
          onEdit={openEditModal}
          onDelete={openDeleteModal}
        />

        {/* Create Discussion Modal */}
        <Modal
          isOpen={isCreateModalOpen}
          onClose={() => setIsCreateModalOpen(false)}
          title="Create New Discussion"
        >
          <DiscussionForm
            onSubmit={handleCreateDiscussion}
            isLoading={isSubmitting}
          />
        </Modal>

        {/* Edit Discussion Modal */}
        <Modal
          isOpen={isEditModalOpen}
          onClose={() => {
            setIsEditModalOpen(false);
            setSelectedDiscussion(null);
          }}
          title="Edit Discussion"
        >
          <DiscussionForm
            onSubmit={handleEditDiscussion}
            initialData={selectedDiscussion}
            isLoading={isSubmitting}
          />
        </Modal>

        {/* Delete Confirmation Modal */}
        <Modal
          isOpen={isDeleteModalOpen}
          onClose={() => {
            setIsDeleteModalOpen(false);
            setSelectedDiscussion(null);
          }}
          title="Delete Discussion"
          footer={
            <>
              <Button
                variant="secondary"
                onClick={() => {
                  setIsDeleteModalOpen(false);
                  setSelectedDiscussion(null);
                }}
                disabled={isSubmitting}
              >
                Cancel
              </Button>
              <Button
                variant="danger"
                onClick={handleDeleteDiscussion}
                disabled={isSubmitting}
              >
                {isSubmitting ? 'Deleting...' : 'Delete'}
              </Button>
            </>
          }
        >
          <p>
            Are you sure you want to delete "{selectedDiscussion?.name}"?
            This will also delete all associated files and chat history.
          </p>
          <p style={{ color: 'var(--accent-magenta)', marginTop: 'var(--spacing-m)' }}>
            This action cannot be undone.
          </p>
        </Modal>
      </div>
    </div>
  );
};

export default HomePage;

