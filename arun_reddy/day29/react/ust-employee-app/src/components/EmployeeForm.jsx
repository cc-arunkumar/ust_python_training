import { useState } from "react";
import api from "../api/api";

function EmployeeForm({ onEmployeeAdded }) {
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!employee.name || !employee.designation) {
      setError("Name and Designation are required");
      return;
    }

    setLoading(true);
    setError("");

    api
      .post("/employees", employee)
      .then((response) => {
        console.log(response.data);
        onEmployeeAdded(response.data);
        setEmployee({ name: "", designation: "", location: "", project: "" });
      })
      .catch((err) => {
        console.error("Error adding employee:", err);
        setError("Failed to add employee");
      })
      .finally(() => setLoading(false));
  };

  return (
    <div className="employee-form">
      <h3>Add New Employee</h3>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={employee.name}
          onChange={handleChange}
          className="input-field"
        />{" "}
        <br />
        <br />
        <input
          type="text"
          name="designation"
          placeholder="Designation"
          value={employee.designation}
          onChange={handleChange}
          className="input-field"
        />{" "}
        <br />
        <br />
        <input
          type="text"
          name="location"
          placeholder="Location"
          value={employee.location}
          onChange={handleChange}
          className="input-field"
        />{" "}
        <br />
        <br />
        <input
          type="text"
          name="project"
          placeholder="Project"
          value={employee.project}
          onChange={handleChange}
          className="input-field"
        />{" "}
        <br />
        <br />
        <button type="submit" disabled={loading} className="submit-button">
          {loading ? "Adding..." : "Add Employee"}
        </button>
      </form>
    </div>
  );
}

export default EmployeeForm;
