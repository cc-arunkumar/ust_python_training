import { useEffect, useState } from "react";
import api from "../api/api";

function EmployeeList({ onEdit }) {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = () => {
    api
      .get("/employees")
      .then((res) => {
        setEmployees(res.data);
      })
      .catch((err) => {
        console.error("Error fetching employees", err);
      })
      .finally(() => setLoading(false));
  };

  const handleDelete = (id) => {
    if (!window.confirm("Delete this employee?")) return;

    api
      .delete(`/employees/${id}`)
      .then(() => {
        setEmployees(employees.filter((emp) => emp.id !== id));
      })
      .catch((err) => console.error("Delete failed", err));
  };

  if (loading) return <p>Loading employees...</p>;

  return (
    <div>
      <h3>Employee List</h3>

      {employees.length === 0 && <p>No employees found</p>}

      {employees.map((emp) => (
        <div key={emp.id} className="employee-card">
          <p>
            <b>{emp.name}</b> - {emp.designation}
          </p>
          <p>
            {emp.location} | {emp.project}
          </p>

          <button onClick={() => onEdit(emp)}>Edit</button>
          <button onClick={() => handleDelete(emp.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}

export default EmployeeList;
