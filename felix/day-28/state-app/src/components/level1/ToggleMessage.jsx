import { useState } from 'react';
import './ToggleMessage.css'

export default function ToggleMessage() {
  const [showMessage, setShowMessage] = useState(false);

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">2. Toggle Message</h3>
      <button 
        onClick={() => setShowMessage(!showMessage)} 
        className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 mb-3"
      >
        {showMessage ? 'Hide' : 'Show'} Message
      </button>
      {showMessage && (
        <div className="bg-blue-50 border border-blue-200 p-3 rounded text-center text-blue-700">
          Welcome to UST Dashboard!
        </div>
      )}
    </div>
  );
}