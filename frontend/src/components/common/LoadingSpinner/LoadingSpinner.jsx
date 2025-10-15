import './LoadingSpinner.css';

const LoadingSpinner = ({ size = 'medium', message = null }) => {
  return (
    <div className="spinner-container">
      <div className={`spinner spinner--${size}`}></div>
      {message && <p className="spinner__message">{message}</p>}
    </div>
  );
};

export default LoadingSpinner;

