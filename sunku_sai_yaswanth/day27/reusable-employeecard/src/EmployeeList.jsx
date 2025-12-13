import React from "react";
import EmployeeCard from "./EmployeeCard";
import ranbirImage from './assets/ranbir.webp'

function EmployeeList() {
  return (
    <div>
      <h1>Employee List</h1>
      <EmployeeCard name="Arjun" employeeid={101} role="IT" location="Kochi"  image={ranbirImage}/>
      <EmployeeCard
        name="charan"
        employeeid={102}
        role="HR"
        location="Hydrabad"
        image={ranbirImage}
      />
      <EmployeeCard name="sai" employeeid={101} role="IT" location="Banglore" image={ranbirImage}/>
      <EmployeeCard
        name="vamshi"
        employeeid={102}
        role="IT"
        location="Trivandram"
        image={ranbirImage}
      />
    </div>
  );
}

export default EmployeeList;
