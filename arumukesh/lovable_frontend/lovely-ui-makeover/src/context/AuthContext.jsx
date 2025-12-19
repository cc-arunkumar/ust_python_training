import React, { createContext, useState, useContext, useEffect } from 'react'
import { jwtDecode } from 'jwt-decode'
import api from '../services/api'

const AuthContext = createContext(null)

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      try {
        const decoded = jwtDecode(token)
        
        // Check if token is expired
        if (decoded.exp * 1000 < Date.now()) {
          localStorage.removeItem('token')
          setUser(null)
        } else {
          // Set user from decoded token
          setUser({
            emp_id: decoded.sub,
            roles: decoded.roles || [],
          })
          // Set axios default header
          api.defaults.headers.common['Authorization'] = `Bearer ${token}`
        }
      } catch (error) {
        console.error('Invalid token:', error)
        localStorage.removeItem('token')
        setUser(null)
      }
    }
    setLoading(false)
  }, [])

  const login = (token, userData) => {
    localStorage.setItem('token', token)
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`
    
    const decoded = jwtDecode(token)
    setUser({
      emp_id: decoded.sub,
      roles: decoded.roles || [],
    })
  }

  const logout = () => {
    localStorage.removeItem('token')
    delete api.defaults.headers.common['Authorization']
    setUser(null)
  }

  const hasRole = (role) => {
    if (!user || !user.roles) return false
    return user.roles.some(r => r.toLowerCase() === role.toLowerCase())
  }

  const isAdmin = () => hasRole('admin')
  const isManager = () => hasRole('manager')
  const isDeveloper = () => hasRole('developer')

  const value = {
    user,
    login,
    logout,
    loading,
    hasRole,
    isAdmin,
    isManager,
    isDeveloper,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider')
  }
  return context
}