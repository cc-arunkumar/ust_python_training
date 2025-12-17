import React, { useState, useEffect } from 'react';
import LoginScreen from './components/auth/LoginScreen';
import Dashboard from './pages/Dashboard';
import { getToken, getUserData, setToken, setUserData, clearAuthData } from './utils/helpers';

function App() {
  const [authData, setAuthData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check for existing auth data on mount
    const token = getToken();
    const userData = getUserData();
    
    if (token && userData) {
      setAuthData({ token, user: userData });
    }
    
    setLoading(false);
  }, []);

  const handleLogin = (data) => {
    setToken(data.token);
    setUserData(data.user);
    setAuthData(data);
  };

  const handleLogout = () => {
    clearAuthData();
    setAuthData(null);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (!authData) {
    return <LoginScreen onLogin={handleLogin} />;
  }

  return <Dashboard user={authData.user} onLogout={handleLogout} />;
}

export default App;