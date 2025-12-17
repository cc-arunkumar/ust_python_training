import React from 'react';
import { AuthProvider } from './contexts/AuthContext';
import AppRouter from './components/AppRouter';
import { BrowserRouter } from 'react-router-dom';

const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRouter />
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;
