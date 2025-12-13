// import React from 'react'
// import EmployeeCard from './EmployeeCard'
 
// const ProjectTeam = () => {
//   return (
//     <div>
//         <EmployeeCard name="Abhi" employeeid={9051} role="SDE" location="Trivandum"/>
//         <EmployeeCard name="Sai" employeeid={1234} role="SDE" location="Kochi"/>
//        <EmployeeCard name="Shakeel" employeeid={9876} role="SDE" location="Pulivendula"/>
     
//     </div>
//   )
// }
 
// export default ProjectTeam
 



// ProjectTeam.jsx
import React from 'react';
import EmployeeCard from './EmployeeCard';

const ProjectTeam = () => {
  return (
    <div>
      <EmployeeCard name="Abhi" employeeid={9051} role="SDE" location="Trivandrum" />
      <EmployeeCard name="Sai" employeeid={1234} role="SDE" location="Kochi" />
      <EmployeeCard name="Shakeel" employeeid={9876} role="SDE" location="Pulivendula" />
    </div>
  );
};

export default ProjectTeam;
