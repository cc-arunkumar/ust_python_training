import { useEffect, useState } from "react";
import api from "../api/api";

function GetEmployees() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    api
      .get("/employees")
      .then((res) => setEmployees(res.data))
      .catch((err) => console.error("Error fetching employees:", err));
  }, []);

  return (
    <div>
      <h2>All Employees</h2>
      <ul>
        {employees.map((emp) => (
          <li key={emp.id}>
            {emp.name} - {emp.designation} - {emp.location} - {emp.project}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GetEmployees;
