import React, { useState } from 'react';
import { Login } from './components/Login';
import { Dashboard } from './components/Dashboard';

export default function App() {
  const [token, setToken] = useState(null);
  const [username, setUsername] = useState('');

  const handleLogin = (accessToken, user) => {
    setToken(accessToken);
    setUsername(user);
  };

  const handleLogout = () => {
    setToken(null);
    setUsername('');
  };

  return token ? (
    <Dashboard token={token} username={username} onLogout={handleLogout} />
  ) : (
    <Login onLogin={handleLogin} />
  );
}