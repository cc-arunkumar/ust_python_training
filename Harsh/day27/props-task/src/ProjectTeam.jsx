import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  const team = [
    {
      name: "David Lee",
      employeeId: "T201",
      role: "Team Lead",
      location: "Toronto",
      image: "https://th.bing.com/th/id/OIP.fngfQLqf864JuWBv6ycJpAHaJ4?w=202&h=269&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1",
    },
    {
      name: "Emma Watson",
      employeeId: "T202",
      role: "QA Engineer",
      location: "Sydney",
      image:
        "https://th.bing.com/th/id/OIP.cTAOjjw9VxkRt1hmIDnP8QHaE8?w=247&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1",
    },
  ];

  return (
    <div className="Project">
      {team.map((member) => (
        <EmployeeCard
          image={member.image}
          name={member.name}
          employeeId={member.employeeId}
          role={member.role}
          location={member.location}
        />
      ))}
    </div>
  );
};

export default ProjectTeam;
