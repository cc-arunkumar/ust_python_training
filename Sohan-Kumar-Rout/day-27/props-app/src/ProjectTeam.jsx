import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  return (
    <div>
      <h1>Project Team</h1>

      <div style={{ display: "flex", flexWrap: "wrap" }}>
        <EmployeeCard 
          name="Praveen" 
          employeeId="EMP201" 
          role="Developer-1" 
          location="Hyderabad" 
        />

        <EmployeeCard 
          name="Prithvi" 
          employeeId="EMP202" 
          role="QA Engineer" 
          location="Chennai" 
        />

        <EmployeeCard 
          name="Rohit" 
          employeeId="EMP203" 
          role="DevOps Engineer" 
          location="Delhi" 
        />
      </div>
    </div>
  );
};

export default ProjectTeam;
