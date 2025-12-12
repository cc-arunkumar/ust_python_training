import React from "react";
import EmployeeList from "./EmployeeList";
import ProjectTeam from "./ProjectTeam";

function App() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1 className="heading">Company Dashboard</h1>

      {/* Employee List Section */}
      <section>
        <h2 className="Emp">Employee List</h2>
        <EmployeeList />
      </section>

      {/* Project Team Section */}
      <section>
        <h2 className="Project">Project Team</h2>
        <ProjectTeam />
      </section>
    </div>
  );
}

export default App;
