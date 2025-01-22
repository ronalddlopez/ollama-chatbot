import {} from 'react';

const ChatContainer = () => {
    
    return (
        <div id="chat-container" className="d-flex flex-column border bg-white p-3">
          <div id="chat-display" className="flex-grow-1 overflow-auto mb-2">
          </div>
          <div id="typing-indicator" className="text-muted small mb-2"></div>
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              placeholder="Type your message..."
              aria-label="Message input"
            />
            <button 
              id="send-button" 
              className="btn btn-primary" 
              >
              
            </button>
          </div> 
        </div>
      );
    };
    
    export default ChatContainer;
    