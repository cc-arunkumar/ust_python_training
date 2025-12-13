import React from 'react';
import EmployeeList from './EmployeeList';
import EmployeeCard from './EmployeeCard';
import './App.css';

function App() {
  return (
    <div>


      <div className="test"> 
        <h1>
          Project Team Members
        </h1>
        <div className="card-container">
          <EmployeeCard name="Madhan" employeeId="E101" role="Lead Developer" location="Chennai" />
          <EmployeeCard name="gv"  employeeId="E103" role="House Kepping" location="Chennai" />
          <EmployeeCard name="gows"   employeeId="E104" role="Jr Software Dev" location="Chennai" />
        </div>
      </div>
      
      <EmployeeList />
    </div>
  );
}

export default App;