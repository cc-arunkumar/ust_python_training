import React, { createContext, useContext, useState, useEffect } from 'react';
import ApiService from '../services/api';
import { STORAGE_KEYS } from '../utils/constants';

const AuthContext = createContext(null);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [activeRole, setActiveRole] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showRoleSelector, setShowRoleSelector] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    const userData = localStorage.getItem(STORAGE_KEYS.USER);
    const savedRole = localStorage.getItem(STORAGE_KEYS.ACTIVE_ROLE);
    
    if (token && userData) {
      try {
        const parsedUser = JSON.parse(userData);
        setUser(parsedUser);
        
        // Check if user has multiple roles
        const hasMultipleRoles = parsedUser.role && parsedUser.role.length > 1;
        
        if (hasMultipleRoles) {
          // If multiple roles and no saved role, show role selector
          if (savedRole && parsedUser.role.includes(savedRole)) {
            setActiveRole(savedRole);
          } else {
            setShowRoleSelector(true);
          }
        } else if (parsedUser.role && parsedUser.role.length === 1) {
          // Single role - set it automatically
          setActiveRole(parsedUser.role[0]);
          localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, parsedUser.role[0]);
        }
      } catch (error) {
        console.error('Failed to parse user data:', error);
        localStorage.removeItem(STORAGE_KEYS.TOKEN);
        localStorage.removeItem(STORAGE_KEYS.USER);
        localStorage.removeItem(STORAGE_KEYS.ACTIVE_ROLE);
      }
    }
    
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    const response = await ApiService.login(email, password);
    
    localStorage.setItem(STORAGE_KEYS.TOKEN, response.access_token);
    
    // TODO: Get user roles from the actual API response
    // The API should return user roles in the response
    // For now, you need to make another API call to get user details or
    // modify your backend to include role information in the login response
    
    // TEMPORARY: Extract roles from response if available, otherwise default to empty array
    let userRoles = [];
    
    // Check if API response includes role information
    if (response.role) {
      // If role is a string, split it by comma
      if (typeof response.role === 'string') {
        userRoles = response.role.split(',').map(r => r.trim());
      } else if (Array.isArray(response.role)) {
        userRoles = response.role;
      }
    } else if (response.roles) {
      // Alternative: check for 'roles' property
      userRoles = Array.isArray(response.roles) ? response.roles : [response.roles];
    }
    
    // If no roles found in response, you need to fetch user details
    // This is a placeholder - replace with actual API call
    if (userRoles.length === 0) {
      console.warn('No roles found in login response. Please update your backend to include role information.');
      // You might want to make an additional API call here to get user details
      // const userDetails = await ApiService.getCurrentUser();
      // userRoles = userDetails.role;
      
      // For testing purposes only - REMOVE THIS IN PRODUCTION
      userRoles = ['DEVELOPER']; // Default fallback
    }
    
    const userData = { 
      email, 
      role: userRoles
    };
    
    localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(userData));
    setUser(userData);
    
    // Check if user has multiple roles
    const hasMultipleRoles = userRoles.length > 1;
    
    if (hasMultipleRoles) {
      // Show role selector if multiple roles
      setShowRoleSelector(true);
    } else {
      // Single role - set it automatically
      setActiveRole(userRoles[0]);
      localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, userRoles[0]);
    }
    
    return userData;
  };

  const selectRole = (role) => {
    setActiveRole(role);
    localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, role);
    setShowRoleSelector(false);
  };

  const changeRole = () => {
    // Only allow role change if user has multiple roles
    if (user && user.role && user.role.length > 1) {
      setShowRoleSelector(true);
    }
  };

  const logout = () => {
    localStorage.removeItem(STORAGE_KEYS.TOKEN);
    localStorage.removeItem(STORAGE_KEYS.USER);
    localStorage.removeItem(STORAGE_KEYS.ACTIVE_ROLE);
    setUser(null);
    setActiveRole(null);
    setShowRoleSelector(false);
  };

  const hasRole = (role) => {
    return activeRole === role;
  };

  const hasMultipleRoles = () => {
    return user && user.role && user.role.length > 1;
  };

  const value = {
    user,
    activeRole,
    login,
    logout,
    loading,
    hasRole,
    hasMultipleRoles,
    showRoleSelector,
    selectRole,
    changeRole
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};