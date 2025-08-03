const { useState, useRef, useEffect } = React;

function ChatApp() {
  const [messages, setMessages] = useState([
    { sender: "Brampton", text: "Hello! I'm Brampton, your finance AI assistant. Ask me anything about investing, markets, economics, or financial planning!" }
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = inputValue.trim();
    setInputValue("");
    setMessages(prev => [...prev, { sender: "You", text: userMessage }]);
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setMessages(prev => [...prev, { sender: "Brampton", text: data.response }]);
    } catch (error) {
      console.error("Error:", error);
      setMessages(prev => [...prev, { 
        sender: "Brampton", 
        text: "Sorry, I'm having trouble connecting to the server. Please make sure the backend is running on localhost:8000 and Ollama is running." 
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900">
      {/* Header */}
      <div className="bg-gray-800 border-b border-gray-700 p-4">
        <div className="max-w-4xl mx-auto flex items-center">
          <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center mr-3">
            <span className="text-white font-bold">💼</span>
          </div>
          <h1 className="text-xl font-semibold text-white">Brampton Finance AI</h1>
          <div className="ml-auto text-sm text-gray-400">
            Powered by Ollama 3.1
          </div>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4">
        <div className="max-w-4xl mx-auto space-y-4">
          {messages.map((message, index) => (
            <div key={index} className={`flex ${message.sender === "You" ? "justify-end" : "justify-start"}`}>
              <div className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                message.sender === "You" 
                  ? "bg-blue-600 text-white" 
                  : "bg-gray-700 text-white"
              }`}>
                <div className="text-xs opacity-75 mb-1">{message.sender}</div>
                <div className="whitespace-pre-wrap">{message.text}</div>
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-gray-700 text-white max-w-xs lg:max-w-md px-4 py-2 rounded-lg">
                <div className="text-xs opacity-75 mb-1">Brampton</div>
                <div className="flex items-center space-x-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                </div>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input */}
      <div className="bg-gray-800 border-t border-gray-700 p-4">
        <div className="max-w-4xl mx-auto flex space-x-4">
          <textarea
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask about stocks, investments, market trends..."
            className="flex-1 p-3 bg-gray-700 text-white rounded-lg border border-gray-600 focus:border-blue-500 focus:outline-none resize-none"
            rows="1"
            disabled={isLoading}
          />
          <button
            onClick={sendMessage}
            disabled={!inputValue.trim() || isLoading}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {isLoading ? "..." : "Send"}
          </button>
        </div>
      </div>
    </div>
  );
}

ReactDOM.render(<ChatApp />, document.getElementById('root'));
