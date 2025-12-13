import React from "react";
import EmployeeCard from "./EmployeeCard";
import './App.css';

function App() {
  return (
    <div className="min-h-screen bg-cover bg-fixed p-8" style={{ backgroundImage: "url('header.png')" }}>
      <h1 className="card1">Employee Dashboard</h1>

      <section className="mb-12">
        <h2>Employee List</h2>
        <div className="cards-container">
          <EmployeeCard className="employee-card" name="Arun" employeeId="E101" role="Developer" location="Mumbai" />
          <EmployeeCard className="employee-card" name="Sohan" employeeId="E102" role="Designer" location="Delhi" />
          <EmployeeCard className="employee-card" name="Sovan" employeeId="E103" role="Tester" location="Pune" />
        </div>
      </section>
      <section>
        <h2>Project Team</h2>
        <div className="cards-container">
          <EmployeeCard className="employee-card" name="Rahul" employeeId="T201" role="Team Lead" location="Bangalore" />
          <EmployeeCard className="employee-card" name="Anita" employeeId="T202" role="Backend Dev" location="Hyderabad" />
        </div>
      </section>
    </div>
  );
}

export default App;
