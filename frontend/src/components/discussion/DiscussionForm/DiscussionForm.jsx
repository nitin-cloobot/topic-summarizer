import { useState } from 'react';
import Button from '../../common/Button/Button';
import ErrorMessage from '../../common/ErrorMessage/ErrorMessage';
import './DiscussionForm.css';

const DiscussionForm = ({ onSubmit, initialData = null, isLoading = false }) => {
  const [name, setName] = useState(initialData?.name || '');
  const [description, setDescription] = useState(initialData?.description || '');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!name.trim()) {
      setError('Discussion name is required');
      return;
    }
    
    setError('');
    onSubmit({ name: name.trim(), description: description.trim() });
  };

  return (
    <form className="discussion-form" onSubmit={handleSubmit}>
      {error && <ErrorMessage message={error} onDismiss={() => setError('')} />}
      
      <div className="form-group">
        <label htmlFor="name" className="form-label">
          Discussion Name <span className="required">*</span>
        </label>
        <input
          type="text"
          id="name"
          className="form-input"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter discussion name"
          disabled={isLoading}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="description" className="form-label">
          Description (Optional)
        </label>
        <textarea
          id="description"
          className="form-textarea"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Enter description"
          rows="4"
          disabled={isLoading}
        />
      </div>

      <Button
        type="submit"
        variant="primary"
        fullWidth
        disabled={isLoading}
      >
        {isLoading ? 'Saving...' : (initialData ? 'Update Discussion' : 'Create Discussion')}
      </Button>
    </form>
  );
};

export default DiscussionForm;

