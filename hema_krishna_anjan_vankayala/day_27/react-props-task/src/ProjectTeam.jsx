import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  const team = [
    { name: "Ravi", employeeId: "T201", role: "Team Lead", location: "Chennai" },
    { name: "Priya Prakash", employeeId: "T202", role: "Backend Dev", location: "Mumbai" },
    { name: "Johnson", employeeId: "T203", role: "Frontend Dev", location: "Delhi" },
  ];

  return (
    <div className="section">
      <h2 className="section-title">Project Team</h2>

      <div className="card-container">
        {team.map((member) => (
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
