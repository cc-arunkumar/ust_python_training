import api from './api'

export const employeeApi = {
  // Get all employees
  getAllEmployees: async () => {
    const response = await api.get('/api/v1/employees')
    return response.data
  },

  // Get employee by ID
  getEmployeeById: async (empId) => {
    const response = await api.get(`/api/v1/employees/${empId}`)
    return response.data
  },

  // Create employee
  createEmployee: async (employeeData) => {
    const response = await api.post('/api/v1/employees', employeeData)
    return response.data
  },

  // Update employee
  updateEmployee: async (empId, employeeData) => {
    const response = await api.put(`/api/v1/employees/${empId}`, employeeData)
    return response.data
  },

  // Delete employee
  deleteEmployee: async (empId) => {
    const response = await api.delete(`/api/v1/employees/${empId}`)
    return response.data
  },
}

export default employeeApi