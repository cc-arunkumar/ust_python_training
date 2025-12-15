import React from 'react'
import './App.css' // or EmployeeCard.css if you prefer separate styling

const EmployeeCard = ({ name, employeeId, role, location }) => {
  return (
    <div className="employee-card">
      <h2 className="employee-name">{name}</h2>
      <p><strong>ID:</strong> {employeeId}</p>
      <p><strong>Role:</strong> {role}</p>
      <p><strong>Location:</strong> {location}</p>
    </div>
  )
}

export default EmployeeCard
