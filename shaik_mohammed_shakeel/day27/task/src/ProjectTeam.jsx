import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  return (
    <div>
      <EmployeeCard
        img="./pexels-brianpxd-35133055.jpg"
        name="Shakeel"
        employeeid={9051}
        role="SDE"
        location="Trivandum"
      />
      <EmployeeCard
        img="./pexels-brianpxd-35133055.jpg"
        name="Sai"
        employeeid={1234}
        role="SDE"
        location="Kochi"
      />
      <EmployeeCard
        img="./pexels-brianpxd-35133055.jpg"
        name="Abhi"
        employeeid={9876}
        role="SDE"
        location="Chilamkur"
      />
    </div>
  );
};

export default ProjectTeam;
