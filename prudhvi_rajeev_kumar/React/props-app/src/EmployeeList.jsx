import React from 'react'
import EmployeeCard from './EmployeeCard'

const EmployeeList = () => {
  return (
    <div className="cards-container">
      <EmployeeCard 
        name="Prithvi Rajeev" 
        employeeId="EMP001" 
        role="Full Stack Developer" 
        location="Trivandrum, KL"
        imageUrl="" 
      />
      <EmployeeCard 
        name="Harsh Jaiswal" 
        employeeId="EMP002" 
        role="Backend Developer" 
        location="Hyderabad, TG" 
      />
      <EmployeeCard 
        name="Alice Brown" 
        employeeId="EMP005" 
        role="Programmer Analyst" 
        location="Trivandrum, KL" 
      />
    </div>
  )
}

export default EmployeeList
