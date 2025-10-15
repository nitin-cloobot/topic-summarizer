import { useState } from 'react';
import Button from '../../common/Button/Button';
import './MessageInput.css';

const MessageInput = ({ onSend, isDisabled = false }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (message.trim() && !isDisabled) {
      onSend(message.trim());
      setMessage('');
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form className="message-input" onSubmit={handleSubmit}>
      <div className="message-input__wrapper">
        <textarea
          className="message-input__field"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
          disabled={isDisabled}
          rows="1"
        />
        <Button
          type="submit"
          variant="primary"
          icon="send"
          disabled={!message.trim() || isDisabled}
        >
          Send
        </Button>
      </div>
    </form>
  );
};

export default MessageInput;

