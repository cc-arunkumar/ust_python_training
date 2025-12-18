import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import LoginPage from './auth/LoginPage';
import Dashboard from './dashboard/Dashboard';
import EmployeeManagement from './dashboard/EmployeeManagement';
import UserManagement from './dashboard/UserManagement'; // ADD THIS IMPORT

const AppRouter = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <Routes>
      {!user ? (
        <Route path="*" element={<LoginPage />} />
      ) : (
        <>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/employees" element={<EmployeeManagement />} />
          <Route path="/users" element={<UserManagement />} /> {/* ADD THIS ROUTE */}
          <Route path="*" element={<Dashboard />} /> {/* fallback */}
        </>
      )}
    </Routes>
  );
};

export default AppRouter;