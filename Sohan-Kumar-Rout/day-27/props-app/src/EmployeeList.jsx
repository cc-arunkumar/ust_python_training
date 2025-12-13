import React from "react";
import EmployeeCard from "./EmployeeCard";

const EmployeeList = () => {
  return (
    <div>
      <h1>Employee List</h1>

      <div style={{ display: "flex", flexWrap: "wrap" }}>
        <EmployeeCard 
          name="Sohan Kumar" 
          employeeId="EMP101" 
          role="Frontend Developer" 
          location="Bhubaneswar" 
        />

        <EmployeeCard 
          name="Sovan Mohanty" 
          employeeId="EMP102" 
          role="Backend Developer" 
          location="Pune" 
        />

        <EmployeeCard 
          name="Itishree Das" 
          employeeId="EMP103" 
          role="UI/UX Designer" 
          location="Bangalore" 
        />
      </div>
    </div>
  );
};

export default EmployeeList;
