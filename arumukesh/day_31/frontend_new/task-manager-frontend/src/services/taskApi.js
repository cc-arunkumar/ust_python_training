import api from './api'

export const taskApi = {
  // Get all tasks
  getAllTasks: async () => {
    const response = await api.get('/api/v1/tasks')
    return response.data
  },

  // Get task by ID
  getTaskById: async (taskId) => {
    const response = await api.get(`/api/v1/tasks/${taskId}`)
    return response.data
  },

  // Create task
  createTask: async (taskData) => {
    const response = await api.post('/api/v1/tasks', taskData)
    return response.data
  },

  // Update task (non-status fields)
  updateTask: async (taskId, taskData) => {
    const response = await api.put(`/api/v1/tasks/${taskId}`, taskData)
    return response.data
  },

  // Update task status
  updateTaskStatus: async (taskId, status) => {
    const response = await api.patch(`/api/v1/tasks/${taskId}/status`, {
      t_id: taskId,
      status: status,
    })
    return response.data
  },

  // Update task priority
  updateTaskPriority: async (taskId, priority) => {
    const response = await api.patch(`/api/v1/tasks/${taskId}/priority`, {
      priority: priority,
    })
    return response.data
  },

  // Delete task
  deleteTask: async (taskId) => {
    const response = await api.delete(`/api/v1/tasks/${taskId}`)
    return response.data
  },
}

export default taskApi