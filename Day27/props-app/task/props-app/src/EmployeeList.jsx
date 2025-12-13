import React from 'react';
import EmployeeCard from './EmployeeCard';
import './App.css';

const EmployeeList = () => {
  return (
    <div className='test'>
      <h1>
        Employee List
      </h1>

      <div className="card-container">
        <EmployeeCard name="Arun" employeeId="101" role="Master in Full-Stack" location="Banglore" />
        <EmployeeCard name="Nivya" employeeId="102" role="Human Resource" location="Trivandrum" />
        <EmployeeCard name="Jennie"  employeeId="103" role="UI/UX Designer" location="Mumbai" />
        <EmployeeCard name="Sai"   employeeId="104" role="Project Manager" location="Chennai" />
      </div>
    </div>
  );
};

export default EmployeeList;