import React from "react";
import EmployeeList from "./EmployeeList";
import ProjectTeam from "./ProjectTeam";
import "./index.css";

const App = () => {
  return (
    <div>
      <h1 className="main-title">Employee Dashboard</h1>

      <EmployeeList />
      <ProjectTeam />
    </div>
  );
};

export default App;
