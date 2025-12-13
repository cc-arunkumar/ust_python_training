// ProjectTeam.jsx
import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  // Sample project team data with image URLs
  const teamMembers = [
    {
      name: "Shero",
      employeeId: "789",
      role: "UI/UX Designer",
      location: "London",
      imageUrl:
        "https://www.bing.com/th/id/OIP._GPUZCqaUNeMLjr8KN1YbwHaEK?w=242&h=211&c=8&rs=1&qlt=90&o=6&cb=ucfimg1&pid=3.1&rm=2&ucfimg=1", // Example image URL
    },
    {
      name: "Appa",
      employeeId: "101",
      role: "Backend Developer",
      location: "Berlin",
      imageUrl:
        "https://i.pinimg.com/736x/25/5b/21/255b21b3bee32b2bf927cb65ebe03e4c.jpg", // Example image URL
    },
  ];

  return (
    <div className="project-team">
      {teamMembers.map((member) => (
        <EmployeeCard
          key={member.employeeId}
          name={member.name}
          employeeId={member.employeeId}
          role={member.role}
          location={member.location}
          imageUrl={member.imageUrl} // Pass image URL to EmployeeCard
        />
      ))}
    </div>
  );
};

export default ProjectTeam;
