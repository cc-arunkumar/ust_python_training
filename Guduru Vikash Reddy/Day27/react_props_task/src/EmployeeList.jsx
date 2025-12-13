import React from "react";
import EmployeeCard from "./EmployeeCard";
 
const EmployeeList = () => {
  const employees = [
    { name: "anjan", employeeId: "E101", role: "Developer", location: "trivandrum" },
    { name: "madan", employeeId: "E102", role: "Tester", location: "Hyderabad" },
    { name: "punju", employeeId: "E103", role: "Hr", location: "Bangalore" },
  ];
 
  return (
    <div className="section">
      <h2 className="section-title">Employee List</h2>
 
      <div className="card-container">
        {employees.map((emp) => (
          <EmployeeCard
            key={emp.employeeId}
            name={emp.name}
            employeeId={emp.employeeId}
            role={emp.role}
            location={emp.location}
          />
        ))}
      </div>
    </div>
  );
};
 
export default EmployeeList;
