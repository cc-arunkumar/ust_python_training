import { useState } from "react";
import api from "../api/api";

function DeleteEmployee() {
  const [employeeId, setEmployeeId] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleDelete = () => {
    if (!employeeId) {
      setError("Employee ID is required");
      return;
    }

    setError("");
    api
      .delete(`/employees/${employeeId}`)
      .then(() => {
        setMessage("Employee deleted successfully");
        setEmployeeId("");
      })
      .catch(() => {
        setError("Failed to delete employee");
      });
  };

  return (
    <div className="employee-form">
      <h3>Delete Employee</h3>

      {error && <p className="error">{error}</p>}
      {message && <p className="success">{message}</p>}

      <input
        type="text"
        placeholder="Employee ID"
        value={employeeId}
        onChange={(e) => setEmployeeId(e.target.value)}
        className="input-field"
      />
      <br /><br />

      <button onClick={handleDelete} className="delete-button">
        Delete Employee
      </button>
    </div>
  );
}

export default DeleteEmployee;
