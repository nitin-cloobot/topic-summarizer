import DiscussionCard from '../DiscussionCard/DiscussionCard';
import LoadingSpinner from '../../common/LoadingSpinner/LoadingSpinner';
import './DiscussionList.css';

const DiscussionList = ({ discussions, isLoading, onEdit, onDelete }) => {
  if (isLoading) {
    return <LoadingSpinner message="Loading discussions..." />;
  }

  if (discussions.length === 0) {
    return (
      <div className="discussion-list-empty">
        <span className="material-symbols-outlined discussion-list-empty__icon">
          chat_bubble
        </span>
        <h3>No Discussions Yet</h3>
        <p>Create your first discussion to get started</p>
      </div>
    );
  }

  return (
    <div className="discussion-list">
      {discussions.map((discussion) => (
        <DiscussionCard
          key={discussion.id}
          discussion={discussion}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default DiscussionList;

