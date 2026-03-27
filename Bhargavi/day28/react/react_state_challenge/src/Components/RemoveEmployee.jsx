import React, { useState } from "react";

function RemoveEmployee() {
  const [employees, setEmployees] = useState([
    { name: "Alice", role: "Engineer" },
    { name: "Bob", role: "Designer" },
  ]);

  const removeEmployee = (index) => {
    setEmployees(employees.filter((_, i) => i !== index));
  };

  return (
    <div className="box">
      <ul>
        {employees.map((emp, index) => (
          <li key={index}>
            {emp.name} - {emp.role}{" "}
            <button onClick={() => removeEmployee(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RemoveEmployee;
