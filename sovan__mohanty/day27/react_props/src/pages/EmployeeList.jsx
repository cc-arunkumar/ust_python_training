// src/pages/EmployeeList.jsx
import React from "react";
import EmployeeCard from "../components/EmployeeCard";

const EmployeeList = () => {
  const employees = [
    { name: "Arun", employeeId: "E101", role: "Developer", location: "Mumbai" },
    { name: "Sohan", employeeId: "E102", role: "Designer", location: "Delhi" },
    { name: "Sovan", employeeId: "E103", role: "Tester", location: "Pune" },
  ];

  return (
    <div className="employee-list">
      <h2>Employee List</h2>
      <div className="cards-container">
        {employees.map(emp => (
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
