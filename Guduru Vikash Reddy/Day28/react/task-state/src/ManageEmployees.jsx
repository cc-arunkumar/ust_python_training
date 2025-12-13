import React, { useState } from 'react';

const ManageEmployees = () => {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState('');
  const [role, setRole] = useState('');

  const addEmployee = () => {
    setEmployees([...employees, { name, role }]);
    setName('');
    setRole('');
  };

  const removeEmployee = (index) => {
    setEmployees(employees.filter((_, i) => i !== index));
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
          <li key={index}>
            {emp.name} - {emp.role}
            <button onClick={() => removeEmployee(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ManageEmployees;
