import { useEffect, useState } from "react";
import api from "../api/api";
import EmployeeItem from "./EmployeeItem";

function EmployeeList({ onEmployeeUpdated, onEmployeeDeleted }) {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    api.get("/employees")
      .then((res) => setEmployees(res.data))
      .catch((err) => console.error("Error fetching employees:", err));
  }, []);

  return (
    <div>
      <h3>Employees</h3>
      {employees.length === 0 ? (
        <p>No employees found</p>
      ) : (
        employees.map((emp) => (
          <EmployeeItem
            key={emp.id}
            employee={emp}
            onEmployeeUpdated={onEmployeeUpdated}
            onEmployeeDeleted={onEmployeeDeleted}
          />
        ))
      )}
    </div>
  );
}

export default EmployeeList;
