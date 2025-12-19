import api from './api'

export const userApi = {
  // Get all users
  getAllUsers: async () => {
    const response = await api.get('/api/v1/users')
    return response.data
  },

  // Get user by emp_id
  getUserById: async (empId) => {
    const response = await api.get(`/api/v1/users/${empId}`)
    return response.data
  },

  // Create user
  createUser: async (userData) => {
    const response = await api.post('/api/v1/users', userData)
    return response.data
  },

  // Update user
  updateUser: async (empId, userData) => {
    const response = await api.put(`/api/v1/users/${empId}`, userData)
    return response.data
  },

  // Delete user
  deleteUser: async (empId) => {
    const response = await api.delete(`/api/v1/users/${empId}`)
    return response.data
  },
}

export default userApi