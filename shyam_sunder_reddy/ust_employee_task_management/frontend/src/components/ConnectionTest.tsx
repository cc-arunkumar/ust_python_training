import { useEffect, useState } from 'react';
import { testAPIConnection } from '../utils/debug';

const ConnectionTest = () => {
  const [status, setStatus] = useState<'checking' | 'connected' | 'disconnected'>('checking');
  const [message, setMessage] = useState('');

  useEffect(() => {
    const checkConnection = async () => {
      setStatus('checking');
      setMessage('Testing backend connection...');
      
      const connected = await testAPIConnection();
      
      if (connected) {
        setStatus('connected');
        setMessage('✅ Backend is reachable');
      } else {
        setStatus('disconnected');
        setMessage('❌ Cannot reach backend. Make sure it\'s running on http://localhost:8000');
      }
    };

    checkConnection();
    // Check every 5 seconds
    const interval = setInterval(checkConnection, 5000);
    
    return () => clearInterval(interval);
  }, []);

  if (status === 'connected') {
    return null; // Don't show if connected
  }

  return (
    <div className="fixed bottom-4 right-4 bg-yellow-50 border border-yellow-200 rounded-lg p-4 shadow-lg z-50 max-w-sm">
      <div className="flex items-center gap-2">
        {status === 'checking' && (
          <div className="animate-spin rounded-full h-4 w-4 border-t-2 border-b-2 border-yellow-600"></div>
        )}
        {status === 'disconnected' && (
          <span className="text-red-600">⚠️</span>
        )}
        <p className="text-sm text-yellow-800">{message}</p>
      </div>
      <p className="text-xs text-yellow-600 mt-2">
        Backend URL: http://localhost:8000
      </p>
    </div>
  );
};

export default ConnectionTest;


