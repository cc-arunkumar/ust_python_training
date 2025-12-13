import React from "react";
import "./index.css"
const EmployeeCard = ({ img, name, employeeid, role, location }) => {
  return (
    <div className="employeecard">
      <img src={img} alt="fortuner pic" className="pic_float" />
      <h2>Name:{name}</h2>
      <h2>Employee ID:{employeeid}</h2>
      <h2>Role: {role}</h2>
      <h2>Location: {location}</h2>
    </div>
  );
};

export default EmployeeCard;
