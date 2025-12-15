import React from 'react'
import EmployeeCard from './EmployeeCard'

const ProjectTeam = () => {
  return (
    <div className="cards-container">
      <EmployeeCard 
        name="Rohit Kumar" 
        employeeId="EMP003" 
        role="UI/UX Designer" 
        location="Bangalore, KA" 
      />
      <EmployeeCard 
        name="Taniya Singh" 
        employeeId="EMP004" 
        role="HR" 
        location="Pune, MH" 
      />
    </div>
  )
}

export default ProjectTeam
