// EmployeeList.jsx
import React from "react";
import EmployeeCard from "./EmployeeCard";

const EmployeeList = () => {
  // Sample employee data with image URLs
  const employees = [
    {
      name: "Bhargavi",
      employeeId: "123",
      role: "Software Engineer",
      location: "New York",
      imageUrl:
        "https://tse1.mm.bing.net/th/id/OIP.hDHvWsCGvbl3SKSG9aSfEwAAAA?cb=ucfimg2&pid=ImgDet&ucfimg=1&w=178&h=250&c=7&o=7&rm=3", // Example image URL
    },
    {
      name: "Meena",
      employeeId: "456",
      role: "Product Manager",
      location: "San Francisco",
      imageUrl:
        "https://tse2.mm.bing.net/th/id/OIP.Sc94M0o6cVTJNqrVKk1vzQHaHa?cb=ucfimg2&pid=ImgDet&ucfimg=1&w=178&h=178&c=7&o=7&rm=3", // Example image URL
    },
  ];

  return (
    <div className="employee-list">
      {employees.map((employee) => (
        <EmployeeCard
          key={employee.employeeId}
          name={employee.name}
          employeeId={employee.employeeId}
          role={employee.role}
          location={employee.location}
          imageUrl={employee.imageUrl} // Pass image URL to EmployeeCard
        />
      ))}
    </div>
  );
};

export default EmployeeList;
