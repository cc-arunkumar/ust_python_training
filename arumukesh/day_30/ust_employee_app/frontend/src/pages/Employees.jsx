import { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../api/employeeApi";
import EmployeeTable from "../components/EmployeeTable";

export default function Employees() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    getEmployees().then(res => setEmployees(res.data));
  }, []);

  const handleDelete = async (id) => {
    await deleteEmployee(id);
    setEmployees(prev => prev.filter(e => e.emp_id !== id));
  };

  return (
    <div className="p-6">
      <EmployeeTable employees={employees} onDelete={handleDelete} />
    </div>
  );
}
