import { useEffect, useState } from "react";
import api from "../api/api";

function EmployeeRead({ onEdit }) {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = () => {
    api
      .get("/employees")
      .then((res) => setEmployees(res.data))
      .catch((err) => console.error(err));
  };

  const handleDelete = (id) => {
    api
      .delete(`/employees/${id}`)
      .then(fetchEmployees)
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <h3>Employees</h3>
      {employees.map((emp) => (
        <div key={emp.id}>
          {emp.name} - {emp.designation}
          <button onClick={() => onEdit(emp)}>Edit</button>
          <button onClick={() => handleDelete(emp.id)}>Delete </button>
        </div>
      ))}
    </div>
  );
}

export default EmployeeRead;
