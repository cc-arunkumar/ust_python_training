// src/pages/ProjectTeam.jsx
import React from "react";
import EmployeeCard from "../components/EmployeeCard";

const ProjectTeam = () => {
  const team = [
    { name: "Rahul", employeeId: "T201", role: "Team Lead", location: "Bangalore" },
    { name: "Anita", employeeId: "T202", role: "Backend Dev", location: "Hyderabad" },
  ];

  return (
    <div className="project-team">
      <h2>Project Team</h2>
      <div className="cards-container">
        {team.map(member => (
          <EmployeeCard
            key={member.employeeId}
            name={member.name}
            employeeId={member.employeeId}
            role={member.role}
            location={member.location}
          />
        ))}
      </div>
    </div>
  );
};

export default ProjectTeam;
