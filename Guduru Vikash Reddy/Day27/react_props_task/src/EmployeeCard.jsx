import React from "react";
 
const EmployeeCard = ({ name, employeeId, role, location }) => {
  return (
    <div className="employee-card">
      <h3 className="employee-name">{name}</h3>
      <p><strong>ID:</strong> {employeeId}</p>
      <p><strong>Role:</strong> {role}</p>
      <p><strong>Location:</strong> {location}</p>
    </div>
  );
};
 
export default EmployeeCard;