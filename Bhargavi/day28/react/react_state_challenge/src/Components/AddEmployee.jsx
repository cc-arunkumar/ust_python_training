import React, { useState } from "react";

function AddEmployee() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    setEmployees([...employees, { name, role }]);
    setName("");
    setRole("");
  };

  return (
    <div className="box">
      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Enter Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />
      <button onClick={addEmployee}>Add Employee</button>
      <ul>
        {employees.map((emp, index) => (
          <li key={index}>
            {emp.name} - {emp.role}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AddEmployee;
