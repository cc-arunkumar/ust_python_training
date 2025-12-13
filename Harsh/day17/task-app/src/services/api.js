import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,  // Get base URL from .env file
})

// Get auth token from localStorage
const getAuthToken = () => {
  return localStorage.getItem('token')  // JWT token stored in localStorage
}

// Add authorization header to the request
api.interceptors.request.use((config) => {
  const token = getAuthToken()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`  // Attach JWT token
  }
  return config
})

// Login request using username and password
export const login = (username, password) => {
  return api.post('/login', { username, password })  // Send username and password
}

// Register request using username and password
export const register = (username, password) => {
  return api.post('/register', { username, password })  // Send username and password
}

// Fetch tasks (requires authentication)
export const fetchTasks = () => {
  return api.get('/tasks')
}

// Create a new task (requires authentication)
export const createTask = (taskData) => {
  return api.post('/tasks', taskData)
}
