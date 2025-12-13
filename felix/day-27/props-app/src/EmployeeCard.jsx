import React from 'react'

export default function EmployeeCard({image_url,name,employeeId,role,location} = {...props}) {
  return (
    <div className='employee'>
        <img src={image_url} alt="Profile" className='profile-photo' />
        <div className='employeename'><h2>{name}</h2></div>
        <div className='employeeid'><h3>🆔 Employee ID: {employeeId}</h3></div>
        <div className='role'><h4>💼 Role: {role}</h4></div>
        <div className='location'><h5>📍 Location: {location}</h5></div>
    </div>
  )
}
