import { useNavigate } from 'react-router-dom';
import Button from '../../components/common/Button/Button';
import './NotFoundPage.css';

const NotFoundPage = () => {
  const navigate = useNavigate();

  return (
    <div className="not-found-page">
      <div className="not-found-page__content">
        <span className="material-symbols-outlined not-found-page__icon">
          error_outline
        </span>
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <Button
          variant="primary"
          icon="home"
          onClick={() => navigate('/')}
        >
          Go to Home
        </Button>
      </div>
    </div>
  );
};

export default NotFoundPage;

