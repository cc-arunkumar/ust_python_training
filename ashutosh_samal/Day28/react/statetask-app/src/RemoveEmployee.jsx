import React, { useState } from "react";

const RemoveEmployee = () => {
  const [employees, setEmployees] = useState([
    { name: "Alice", role: "Developer" },
    { name: "Bob", role: "Designer" },
  ]);

  const removeEmployee = (name) => {
    setEmployees(employees.filter((emp) => emp.name !== name));
  };

  return (
    <div>
      <ul>
        {employees.map((emp) => (
          <li key={emp.name}>
            {emp.name} - {emp.role}{" "}
            <button onClick={() => removeEmployee(emp.name)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RemoveEmployee;
