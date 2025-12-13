// import React from 'react'
 
// const EmployeeCard = ({name,employeeid,role,location}) => {
//   return (
//     <div className='employeecard'>
//         <h2>Name:{name}</h2>
//         <h2>Employee ID:{employeeid}</h2>
//         <h2>Role: {role}</h2>
//         <h2>Location: {location}</h2>
//     </div>
//   );
// };
 
// export default EmployeeCard
 




import React, { useState } from 'react';
import './EmployeeCard.css'; // Import CSS for the card

const EmployeeCard = ({ name, employeeid, role, location }) => {
  // State to manage the flip effect
  const [flipped, setFlipped] = useState(false);

  // Toggle flip state when the card is clicked
  const handleFlip = () => {
    setFlipped(!flipped);
  };

  return (
    <div className="card-wrapper">
      <div
        className={`employeecard ${flipped ? 'open' : ''}`} 
        onClick={handleFlip} // Toggle flip on click
      >
        <div className="front">
          <h3>{name}</h3>
          <p>Click to view details</p>
        </div>
        <div className="back">
          <h3>Employee Details</h3>
          <p>Employee ID: {employeeid}</p>
          <p>Role: {role}</p>
          <p>Location: {location}</p>
        </div>
      </div>
    </div>
  );
};

export default EmployeeCard;
