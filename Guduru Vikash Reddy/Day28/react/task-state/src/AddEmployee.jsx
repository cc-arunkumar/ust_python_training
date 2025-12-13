import React, { useState } from 'react';

const AddEmployee = () => {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState('');
  const [role, setRole] = useState('');

  const addEmployee = () => {
    setEmployees([...employees, { name, role }]);
    setName('');
    setRole('');
  };

  return (
    <div>
      <input 
        type="text" 
        placeholder="Name" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
      />
      <input 
        type="text" 
        placeholder="Role" 
        value={role} 
        onChange={(e) => setRole(e.target.value)} 
      />
      <button onClick={addEmployee}>Add Employee</button>
      <ul>
        {employees.map((emp, index) => (
          <li key={index}>{emp.name} - {emp.role}</li>
        ))}
      </ul>
    </div>
  );
};

export default AddEmployee;
