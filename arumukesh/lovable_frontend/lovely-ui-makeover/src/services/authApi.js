import api from './api'

export const authApi = {
  login: async (emp_id, password) => {
    const response = await api.post('/login', {
      emp_id: Number(emp_id),
      password,
    })
    return response.data
  },

  getCurrentUser: async () => {
    const response = await api.get('/api/v1/users/me')
    return response.data
  },
}

export default authApi