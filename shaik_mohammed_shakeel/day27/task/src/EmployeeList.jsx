import React from "react";
import EmployeeCard from "./EmployeeCard.jsx";

const EmployeeList = () => {
  return (
    <div>
      <EmployeeCard
        img="./pexels-gasparzaldo-11143608.jpg"
        name="Shakeel"
        employeeid={9051}
        role="SDE"
        location="Trivandum"
      />
      <EmployeeCard
        img="./pexels-gasparzaldo-11143608.jpg"
        name="Abhi"
        employeeid={9051}
        role="SDE"
        location="Chilamkuru"
      />
      <EmployeeCard
        img="./pexels-gasparzaldo-11143608.jpg"
        name="Sai"
        employeeid={9051}
        role="SDE"
        location="Trivandum"
      />
    </div>
  );
};

export default EmployeeList;
