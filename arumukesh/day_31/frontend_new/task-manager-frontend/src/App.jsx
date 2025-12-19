import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuth } from './context/AuthContext'
import ErrorBoundary from './components/ErrorBoundary'
import ProtectedRoute from './components/auth/ProtectedRoute'
import RoleBasedRoute from './components/auth/RoleBasedRoute'
import Layout from './components/layout/Layout'

// Pages
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Tasks from './pages/Tasks'
import CreateTask from './pages/CreateTask'
import Users from './pages/Users'
import Employees from './pages/Employees'
import Profile from './pages/Profile'
import NotFound from './pages/NotFound'

function App() {
  const { user } = useAuth()

  return (
    <ErrorBoundary>
      <Routes>
        <Route path="/login" element={user ? <Navigate to="/dashboard" /> : <Login />} />
        
        <Route element={<ProtectedRoute><Layout /></ProtectedRoute>}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/tasks" element={<Tasks />} />
          <Route 
            path="/tasks/create" 
            element={
              <RoleBasedRoute allowedRoles={['admin', 'manager']}>
                <CreateTask />
              </RoleBasedRoute>
            } 
          />
          <Route 
            path="/users" 
            element={
              <RoleBasedRoute allowedRoles={['admin']}>
                <Users />
              </RoleBasedRoute>
            } 
          />
          <Route 
            path="/employees" 
            element={
              <RoleBasedRoute allowedRoles={['admin']}>
                <Employees />
              </RoleBasedRoute>
            } 
          />
          <Route path="/profile" element={<Profile />} />
        </Route>

        <Route path="/" element={<Navigate to="/dashboard" />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </ErrorBoundary>
  )
}

export default App