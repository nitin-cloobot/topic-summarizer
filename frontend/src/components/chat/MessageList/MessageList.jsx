import { useEffect, useRef } from 'react';
import MessageBubble from '../MessageBubble/MessageBubble';
import LoadingSpinner from '../../common/LoadingSpinner/LoadingSpinner';
import './MessageList.css';

const MessageList = ({ messages, isLoading }) => {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="message-list">
      {messages.length === 0 && !isLoading && (
        <div className="message-list-empty">
          <span className="material-symbols-outlined">chat</span>
          <p>No messages yet. Start a conversation!</p>
        </div>
      )}
      
      {messages.map((message, index) => (
        <MessageBubble
          key={index}
          message={message.text}
          isUser={message.isUser}
        />
      ))}
      
      {isLoading && (
        <div className="message-list__loading">
          <LoadingSpinner size="small" />
        </div>
      )}
      
      <div ref={messagesEndRef} />
    </div>
  );
};

export default MessageList;

