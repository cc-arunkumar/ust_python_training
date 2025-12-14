import React from 'react'
import EmployeeCard from './EmployeeCard'

const ProjectTeam = ({ name, id, role, location }) => {
  return (
    <EmployeeCard
      style={{
        background: 'linear-gradient(to top, #94ab2f, #e1e43d, #f0f3bd)',
      }}
    >
      <h2>Project Team</h2>
      <p>Name : {name}</p>
      <p>Emp ID : {id}</p>
      <p>Role : {role}</p>
      <p>Location : {location}</p>
    </EmployeeCard>
  )
}

export default ProjectTeam