import './ErrorMessage.css';

const ErrorMessage = ({ message, onDismiss = null }) => {
  if (!message) return null;

  return (
    <div className="error-message">
      <span className="material-symbols-outlined error-message__icon">error</span>
      <span className="error-message__text">{message}</span>
      {onDismiss && (
        <button className="error-message__close" onClick={onDismiss}>
          <span className="material-symbols-outlined">close</span>
        </button>
      )}
    </div>
  );
};

export default ErrorMessage;

