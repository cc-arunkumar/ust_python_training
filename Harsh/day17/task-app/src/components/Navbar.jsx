import React from 'react'
import { Link } from 'react-router-dom'

function Navbar() {
  const handleLogout = () => {
    localStorage.removeItem('token')  // Clear JWT token from localStorage
    window.location.reload()  // Reload to go back to login page
  }

  const token = localStorage.getItem('token')  // Check if token exists

  return (
    <nav className="navbar">
      <ul>
        <li><Link to="/">Task List</Link></li>
        {!token ? (
          <>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/register">Register</Link></li>
          </>
        ) : (
          <li><button onClick={handleLogout}>Logout</button></li>
        )}
      </ul>
    </nav>
  )
}

export default Navbar
