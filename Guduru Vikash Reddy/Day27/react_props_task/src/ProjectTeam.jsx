// ProjectTeam.jsx
import React from 'react';
import EmployeeCard from './EmployeeCard';  // Import EmployeeCard component

 
const ProjectTeam = () => {
  const teamMembers = [
    { name: 'malli', employeeId: 'E125', role: 'Designer', location: 'Hyderabad' },
    { name: 'golli', employeeId: 'E126', role: 'Developer', location: 'Trivandrum' },
 
  ];
 
  return (
    <div className="project-team">
      <h2>Project Team</h2>
      {teamMembers.map((member) => (
        <EmployeeCard
          key={member.employeeId}
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
 
 