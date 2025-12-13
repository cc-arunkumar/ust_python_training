import React from "react";
import EmployeeCard from "./EmployeeCard";
function ProjectTeam() {
  return (
    <div>
      <h1>Project Team</h1>
      <EmployeeCard name="Arjun" employeeid={101} role="IT" location="Kochi" />
      <EmployeeCard
        name="charan"
        employeeid={102}
        role="HR"
        location="Hydrabad"
      />
    </div>
  );
}

export default ProjectTeam;
