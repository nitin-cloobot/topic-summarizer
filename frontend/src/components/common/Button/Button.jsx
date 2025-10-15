import './Button.css';

const Button = ({ 
  children, 
  variant = 'secondary', 
  size = 'medium', 
  onClick, 
  disabled = false,
  type = 'button',
  fullWidth = false,
  icon = null
}) => {
  return (
    <button
      type={type}
      className={`btn btn--${variant} btn--${size} ${fullWidth ? 'btn--full-width' : ''}`}
      onClick={onClick}
      disabled={disabled}
    >
      {icon && <span className="material-symbols-outlined btn__icon">{icon}</span>}
      {children}
    </button>
  );
};

export default Button;

