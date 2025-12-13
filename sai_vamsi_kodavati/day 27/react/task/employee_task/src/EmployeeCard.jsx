import React from "react";


const EmployeeCard = ({ name, employeeId, role, location,image}) => {
  return (
    <div className="GreetingCard">
      <img src={image} alt={name} className="profile-pic" />

      
      <h2>{name}</h2>
      <p>Employee ID: {employeeId}</p>
      <p>Role: {role}</p>
      <p>Location: {location}</p>
    </div>
  );
};

export default EmployeeCard;