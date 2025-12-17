import React from 'react';
import { AuthProvider, useAuth } from './context/AuthContext';
import LoginPage from './components/auth/LoginPage';
import RoleSelector from './components/auth/RoleSelector';
import Layout from './components/layout/Layout';

const AppContent = () => {
  const { user, activeRole, loading, showRoleSelector } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mb-4"></div>
          <p className="text-lg text-gray-400">Loading...</p>
        </div>
      </div>
    );
  }

  // Show login if no user
  if (!user) {
    return <LoginPage />;
  }

  // Show role selector if user has multiple roles and needs to select one
  if (showRoleSelector) {
    return <RoleSelector />;
  }

  // Show main app if user is logged in and role is selected
  if (activeRole) {
    return <Layout />;
  }

  // Fallback loading state
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="text-center">
        <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mb-4"></div>
        <p className="text-lg text-gray-400">Initializing...</p>
      </div>
    </div>
  );
};

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;