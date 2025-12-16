import { React, useState } from "react";
import api from "../api/api";

const EmployeeForm = ({ onEmployeeAdded }) => {
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlesubmit = (e) => {
    e.preventDefault();

    if (!employee.name || !employee.designation) {
      setError("Name and designation are required");
      return;
    }

    setLoading(true);
    setError("");
    api
      .post("/employees", employee)
      .then((response) => {
        onEmployeeAdded(response.data);
        setEmployee({ name: "", designation: "", location: "", project: "" });
      })
      .catch((err) => {
        console.log("Error:", err);
        setError("Failed to add employee");
      })
      .finally(() => setLoading(false));
  };
  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  return (
    <>
      <div>
        <form onSubmit={handlesubmit}>
          <input
            type="text"
            name="name"
            value={employee.name}
            placeholder="Name"
            onChange={handleChange}
            className="input-field"
          />
          <br />
          <input
            type="text"
            name="designation"
            value={employee.designation}
            placeholder="Designation"
            onChange={handleChange}
            className="input-field"
          />
          <br />
          <input
            type="text"
            name="location"
            value={employee.location}
            placeholder="Location"
            onChange={handleChange}
            className="input-field"
          />
          <br />
          <input
            type="text"
            name="project"
            value={employee.project}
            placeholder="Project"
            onChange={handleChange}
            className="input-field"
          />
          <br />
          <button type="submit" disabled={loading}>
            {loading?"Loading...":"Add Employee"}</button>
        </form>
      </div>
    </>
  );
};

export default EmployeeForm;
