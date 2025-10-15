import Button from '../../common/Button/Button';
import './DiscussionDetail.css';

const DiscussionDetail = ({ discussion, onEdit }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="discussion-detail">
      <div className="discussion-detail__header">
        <div>
          <h1 className="discussion-detail__title">{discussion.name}</h1>
          {discussion.description && (
            <p className="discussion-detail__description">{discussion.description}</p>
          )}
        </div>
        <Button
          variant="secondary"
          icon="edit"
          onClick={onEdit}
        >
          Edit
        </Button>
      </div>
      <div className="discussion-detail__meta">
        <div className="meta-item">
          <span className="material-symbols-outlined">schedule</span>
          <span>Created: {formatDate(discussion.created_at)}</span>
        </div>
        <div className="meta-item">
          <span className="material-symbols-outlined">update</span>
          <span>Updated: {formatDate(discussion.updated_at)}</span>
        </div>
      </div>
    </div>
  );
};

export default DiscussionDetail;

