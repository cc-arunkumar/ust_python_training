import React from "react";
import EmployeeCard from "./EmployeeCard";


const EmployeeList = () => {
  const employees = [
    { name: "Sai Vamsi", employeeId: "EMP101", role: "Full Stack", location: "Trivandrum",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg' },
    { name: "Shakeel", employeeId: "EMP102", role: "Testing", location: "Chennai",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg'},
    { name: "Shyam", employeeId: "EMP103", role: "FrontEnd", location: "Trivandrum",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg'},
    { name: "Anjan", employeeId: "EMP104", role: "BackEnd", location: "Pune" ,image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg'},

  ];

  return (
    <div >
      <h1>Employee List</h1>
      {employees.map((emp) => (
        <EmployeeCard
          key={emp.employeeId}
          name={emp.name}
          employeeId={emp.employeeId}
          role={emp.role}
          location={emp.location}
          image={emp.image}

         
        />
      ))}
    </div>
  );
};

export default EmployeeList;