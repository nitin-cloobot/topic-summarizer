import { useState, useEffect } from 'react';
import MessageList from '../MessageList/MessageList';
import MessageInput from '../MessageInput/MessageInput';
import ErrorMessage from '../../common/ErrorMessage/ErrorMessage';
import { chatService } from '../../../services/api';
import './ChatInterface.css';

const ChatInterface = ({ discussionId, filesCount }) => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSendMessage = async (messageText) => {
    if (filesCount === 0) {
      setError('Please upload files before starting a chat.');
      return;
    }

    setError('');
    
    // Add user message to the list
    const userMessage = { text: messageText, isUser: true };
    setMessages(prev => [...prev, userMessage]);
    
    setIsLoading(true);
    
    try {
      // Build history for Gemini API
      const history = messages.map(msg => ({
        role: msg.isUser ? 'user' : 'model',
        parts: [{ text: msg.text }]
      }));
      
      const response = await chatService.sendMessage(discussionId, messageText, history);
      
      // Add AI response to the list
      const aiMessage = { text: response.message, isUser: false };
      setMessages(prev => [...prev, aiMessage]);
    } catch (err) {
      setError(err.message || 'Failed to send message');
      // Remove user message if request failed
      setMessages(prev => prev.slice(0, -1));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-interface">
      <div className="chat-interface__header">
        <h3 className="chat-interface__title">
          <span className="material-symbols-outlined">chat</span>
          AI Chat
        </h3>
        {filesCount > 0 && (
          <span className="chat-interface__files-count">
            {filesCount} file(s) loaded
          </span>
        )}
      </div>
      
      {error && (
        <div className="chat-interface__error">
          <ErrorMessage message={error} onDismiss={() => setError('')} />
        </div>
      )}
      
      <MessageList messages={messages} isLoading={isLoading} />
      <MessageInput
        onSend={handleSendMessage}
        isDisabled={isLoading || filesCount === 0}
      />
    </div>
  );
};

export default ChatInterface;

