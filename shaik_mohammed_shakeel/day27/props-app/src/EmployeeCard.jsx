import React from 'react'

const EmployeeCard = ({name,employeeid,role,location}={...props}) => {
  return (
    <div className='employeecard'>
        <h2>{name}</h2>
        <h2>{employeeid}</h2>
        <h2>{role}</h2>
        <h2>{location}</h2>

      
    </div>
  );
};

export default EmployeeCard
