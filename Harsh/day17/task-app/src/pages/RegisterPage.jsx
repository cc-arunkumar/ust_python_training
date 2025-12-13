import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { register } from '../services/api'  // Import register API function

function RegisterPage() {
  const [username, setUsername] = useState('')  // Changed to username
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleRegister = async (e) => {
    e.preventDefault()
    try {
      await register(username, password)  // Pass username instead of email
      navigate('/login')  // Redirect to login page
    } catch (error) {
      alert('Error registering')
    }
  }

  return (
    <div className="form-container">
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
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
        <button type="submit">Register</button>
      </form>
    </div>
  )
}

export default RegisterPage
