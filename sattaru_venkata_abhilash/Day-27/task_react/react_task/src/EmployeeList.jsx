// import React from 'react'
// import EmployeeCard from './EmployeeCard.jsx'
 
// const EmployeeList = () => {
//   return (
//     <div>
//       <EmployeeCard name="Niru" employeeid={9051} role="SDE" location="US"/>
//       <EmployeeCard name="Anjan" employeeid={9051} role="SDE" location="Kadapa"/>
//       <EmployeeCard name="Vikas" employeeid={9051} role="SDE" location="Londan"/>
//     </div>
//   )
// }
 
// export default EmployeeList





// EmployeeList.jsx
import React from 'react';
import EmployeeCard from './EmployeeCard';

const EmployeeList = () => {
  return (
    <div>
      <EmployeeCard name="Niru" employeeid={9051} role="SDE" location="US" />
      <EmployeeCard name="Anjan" employeeid={9051} role="SDE" location="Kadapa" />
      <EmployeeCard name="Vikas" employeeid={9051} role="SDE" location="London" />
    </div>
  );
};

export default EmployeeList;

 