// EmployeeCard.jsx
import React from "react";

const EmployeeCard = ({ name, employeeId, role, location, imageUrl }) => {
  return (
    <div className="employee-card">
      <img src={imageUrl} alt={name} className="employee-image" />
      <h3>{name}</h3>
      <p>
        <strong>Employee ID:</strong> {employeeId}
      </p>
      <p>
        <strong>Role:</strong> {role}
      </p>
      <p>
        <strong>Location:</strong> {location}
      </p>
    </div>
  );
};

export default EmployeeCard;
