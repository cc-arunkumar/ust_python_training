import React from 'react';
import EmployeeCard from './EmployeeCard';
import './App.css';

const ProjectTeam = () => {
  return (
    <>
      <h1 style={{ textAlign: 'center', margin: '40px 0', color: '#333' }}>
        Project Team Members
      </h1>

      <div className="card-container">
        <EmployeeCard 
          name="Madhan"
          employeeId="E101"
          role="Lead Developer"
          location="Chennai"
        />
        <EmployeeCard 
          name="Priya"
          employeeId="E103"
          role="Designer"
          location="Hyderabad"
        />
        <EmployeeCard 
          name="Arun"
          employeeId="E104"
          role="Project Manager"
          location="Chennai"
        />
      </div>
    </>
  );
};

export default ProjectTeam;