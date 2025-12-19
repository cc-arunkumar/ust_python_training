import React from 'react'
import { Navigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

const RoleBasedRoute = ({ children, allowedRoles = [] }) => {
  const { user } = useAuth()

  const hasAccess = allowedRoles.some(role => 
    user?.roles?.map(r => r.toLowerCase()).includes(role.toLowerCase())
  )

  if (!hasAccess) {
    return <Navigate to="/dashboard" replace />
  }

  return children
}

export default RoleBasedRoute