import React from 'react'
import EmployeeCard from './EmployeeCard'
const ProjectTeam = () => {
  return (
    <div>
   <EmployeeCard name="Arun" employee_id={201} role="HR" location="Banglore"></EmployeeCard>
   <EmployeeCard name="Sai" employee_id={202} role="Manager" location="Chennai"></EmployeeCard>
  </div>
  )
}

export default ProjectTeam