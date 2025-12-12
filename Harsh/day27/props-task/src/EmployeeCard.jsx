import React from "react";
import "./EmployeeCard.css"; // optional CSS file for styling

const EmployeeCard = ({ name, employeeId, role, location, image }) => {
  return (
    <div className="employee-card">
      {image && <img src={image} className="image"/>}
      <h2>{name}</h2>
      <p>ID: {employeeId}</p>
      <p>Role: {role}</p>
      <p>Location: {location}</p>
    </div>
  );
};

export default EmployeeCard;
