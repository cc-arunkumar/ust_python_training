import React from "react";

function EmployeeCard({ name, employeeid, role, location, image }) {
  return (
    <div className="card">
    <img src={image} alt="name" style={{borderRadius:'50%',width:'150px'}}/>
      <h3>Name:{name}</h3>
      <h3>Employee ID:{employeeid}</h3>
      <h3>Role:{role}</h3>
      <h3>Location:{location}</h3>
    </div>
  );
}

export default EmployeeCard;
