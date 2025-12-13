import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../services/api'  // Import login API function

function LoginPage() {
  const [username, setUsername] = useState('')  // Changed to username
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      const response = await login(username, password)  // Pass username instead of email
      localStorage.setItem('token', response.data.access_token)  // Store JWT token in localStorage
      navigate('/')  // Redirect to task list
    } catch (error) {
      alert('Error logging in')
    }
  }

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"  // Changed placeholder to Username
          value={username}
          onChange={(e) => setUsername(e.target.value)}  // Bind username
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  )
}

export default LoginPage
