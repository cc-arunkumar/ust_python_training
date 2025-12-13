import React from "react";
import EmployeeCard from "./EmployeeCard";

const ProjectTeam = () => {
  const team = [
    { name: "Abhi", employeeId: "EMP201", role: "Team Lead", location: "Bangalore",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg' },
    { name: "Vikas", employeeId: "EMP202", role: "QA Engineer", location: "Hyderabad",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg' },
    { name: "Yashwanth", employeeId: "EMP203", role: "Manager", location: "Pune",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg' },
    { name: "Niranjan", employeeId: "EMP204", role: "Python Developer", location: "Hyderabad",image:'https://d3lzcn6mbbadaf.cloudfront.net/media/details/1_sOg47NF_N9RyIAu.jpg' },


  ];

  return (
    <div className="ProjectTeam">
      <h1>Project Team</h1>
      {team.map((member) => (
        <EmployeeCard
          key={member.employeeId}
          name={member.name}
          employeeId={member.employeeId}
          role={member.role}
          location={member.location}
          image={member.image}

        />
      ))}
    </div>
  );
};

export default ProjectTeam;