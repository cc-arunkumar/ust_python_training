import React, { createContext, useContext, useState, useEffect } from 'react';
import ApiService from '../services/api';
import { STORAGE_KEYS } from '../utils/constants';

const AuthContext = createContext(null);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [activeRole, setActiveRole] = useState(null);
  const [loading, setLoading] = useState(true);

  // Load user from localStorage on mount
  useEffect(() => {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    const userData = localStorage.getItem(STORAGE_KEYS.USER);
    const savedRole = localStorage.getItem(STORAGE_KEYS.ACTIVE_ROLE);

    if (token && userData) {
      try {
        const parsedUser = JSON.parse(userData);
        setUser(parsedUser);

        // Automatically assign first role if not set
        if (parsedUser.role && parsedUser.role.length > 0) {
          const roleToSet = savedRole && parsedUser.role.includes(savedRole)
            ? savedRole
            : parsedUser.role[0];
          setActiveRole(roleToSet);
          localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, roleToSet);
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
    try {
      const response = await ApiService.login(email, password);

      if (!response || !response.access_token) {
        throw new Error('Invalid credentials');
      }

      // Extract roles
      let userRoles = [];
      if (response.role) {
        userRoles = typeof response.role === 'string'
          ? response.role.split(',').map(r => r.trim())
          : Array.isArray(response.role) ? response.role : [response.role];
      } else if (response.roles) {
        userRoles = Array.isArray(response.roles) ? response.roles : [response.roles];
      }

      if (userRoles.length === 0) userRoles = ['DEVELOPER'];

      const userData = { email, role: userRoles };

      // Store only on successful login
      localStorage.setItem(STORAGE_KEYS.TOKEN, response.access_token);
      localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(userData));

      setUser(userData);

      // Automatically assign first role
      setActiveRole(userRoles[0]);
      localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, userRoles[0]);

      return userData;

    } catch (err) {
      // Clear any partially stored data
      localStorage.removeItem(STORAGE_KEYS.TOKEN);
      localStorage.removeItem(STORAGE_KEYS.USER);
      localStorage.removeItem(STORAGE_KEYS.ACTIVE_ROLE);

      throw new Error('Invalid credentials');
    }
  };

  const changeRole = (role) => {
    if (user && user.role && user.role.includes(role)) {
      setActiveRole(role);
      localStorage.setItem(STORAGE_KEYS.ACTIVE_ROLE, role);
    }
  };

  const logout = () => {
    localStorage.removeItem(STORAGE_KEYS.TOKEN);
    localStorage.removeItem(STORAGE_KEYS.USER);
    localStorage.removeItem(STORAGE_KEYS.ACTIVE_ROLE);
    setUser(null);
    setActiveRole(null);
  };

  const hasRole = (role) => activeRole === role;
  const hasMultipleRoles = () => user && user.role && user.role.length > 1;

  return (
    <AuthContext.Provider value={{
      user,
      activeRole,
      login,
      logout,
      loading,
      hasRole,
      hasMultipleRoles,
      changeRole
    }}>
      {children}
    </AuthContext.Provider>
  );
};
