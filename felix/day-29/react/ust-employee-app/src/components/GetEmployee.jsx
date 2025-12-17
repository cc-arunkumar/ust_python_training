import { useState } from "react";
import api from "../api/api";

function GetEmployee() {
  const [employeeId, setEmployeeId] = useState("");
  const [employee, setEmployee] = useState(null);
  const [error, setError] = useState("");

  const handleFetch = () => {
    if (!employeeId) {
      setError("Employee ID is required");
      return;
    }

    setError("");
    api
      .get(`/employees/${employeeId}`)
      .then((response) => {
        setEmployee(response.data);
      })
      .catch(() => {
        setEmployee(null);
        setError("Employee not found");
      });
  };

  return (
    <div className="employee-form">
      <h3>Get Employee By ID</h3>

      {error && <p className="error">{error}</p>}

      <input
        type="text"
        placeholder="Enter Employee ID"
        value={employeeId}
        onChange={(e) => setEmployeeId(e.target.value)}
        className="input-field"
      />
      <br /><br />

      <button onClick={handleFetch} className="submit-button">
        Fetch Employee
      </button>

      {employee && (
        <div className="employee-details">
          <p><b>Name:</b> {employee.name}</p>
          <p><b>Designation:</b> {employee.designation}</p>
          <p><b>Location:</b> {employee.location}</p>
          <p><b>Project:</b> {employee.project}</p>
        </div>
      )}
    </div>
  );
}

export default GetEmployee;
