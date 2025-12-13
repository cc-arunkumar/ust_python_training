
import React from "react";
import "./EmployeeCard.css"; 

const EmployeeCard = ({ name, employeeId, role, location }) => {
  return (
    <div className="employee-card">
      <h3 className="employee-name"><strong>Name:</strong>{name}</h3>
      <p><strong>ID:</strong> {employeeId}</p>
      <p><strong>Role:</strong> {role}</p>
      <p><strong>Location:</strong> {location}</p>
    </div>
  );
};

export default EmployeeCard;
