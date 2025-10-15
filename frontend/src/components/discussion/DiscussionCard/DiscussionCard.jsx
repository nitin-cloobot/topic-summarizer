import { useNavigate } from 'react-router-dom';
import Button from '../../common/Button/Button';
import './DiscussionCard.css';

const DiscussionCard = ({ discussion, onEdit, onDelete }) => {
  const navigate = useNavigate();

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  return (
    <div className="discussion-card">
      <div 
        className="discussion-card__content"
        onClick={() => navigate(`/discussion/${discussion.id}`)}
      >
        <h3 className="discussion-card__title">{discussion.name}</h3>
        {discussion.description && (
          <p className="discussion-card__description">{discussion.description}</p>
        )}
        <div className="discussion-card__meta">
          <span className="discussion-card__date">
            <span className="material-symbols-outlined">schedule</span>
            {formatDate(discussion.updated_at || discussion.created_at)}
          </span>
        </div>
      </div>
      <div className="discussion-card__actions">
        <Button
          variant="secondary"
          size="small"
          icon="edit"
          onClick={(e) => {
            e.stopPropagation();
            onEdit(discussion);
          }}
        >
          Edit
        </Button>
        <Button
          variant="danger"
          size="small"
          icon="delete"
          onClick={(e) => {
            e.stopPropagation();
            onDelete(discussion);
          }}
        >
          Delete
        </Button>
      </div>
    </div>
  );
};

export default DiscussionCard;

