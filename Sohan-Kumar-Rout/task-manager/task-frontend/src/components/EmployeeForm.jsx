import React, { useEffect, useState } from "react";
import { createEmployee, updateEmployee } from "../services/employeeService";

const initialFormState = {
  name: "",
  email: "",
  designation: "",
  department: "",
  location: "",
  status: "Active",
  salary: "",
  date_of_joining: "",
};

const EmployeeForm = ({ selectedEmployee, onSuccess }) => {
  const [formData, setFormData] = useState(initialFormState);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (selectedEmployee) {
      setFormData(selectedEmployee);
    } else {
      setFormData(initialFormState);
    }
  }, [selectedEmployee]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === "salary" ? Number(value) || "" : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      if (selectedEmployee?.id) {
        await updateEmployee(selectedEmployee.id, formData);
      } else {
        await createEmployee(formData);
      }
      onSuccess();
    } catch (err) {
      console.error(err);
      alert("Error saving employee");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-[#112240] shadow-lg border border-[#1F2A40] rounded-lg p-6 mb-6 text-white">
      <h2 className="text-2xl font-semibold mb-4">
        {selectedEmployee ? "Edit Employee" : "Create Employee"}
      </h2>

      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        {Object.keys(initialFormState).map((field) => (
          <div key={field} className="flex flex-col">
            <label className="font-medium capitalize mb-1">
              {field.replace(/_/g, " ")}
            </label>

            <input
              type={field === "date_of_joining" ? "date" : "text"}
              name={field}
              value={formData[field] || ""}
              onChange={handleChange}
              className="bg-[#0A1A2F] border border-[#1F2A40] text-white rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />
          </div>
        ))}

        <div className="col-span-2 flex gap-4 mt-4">
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded text-white font-semibold"
          >
            {loading ? "Saving..." : selectedEmployee ? "Update" : "Create"}
          </button>

          <button
            type="button"
            onClick={() => setFormData(initialFormState)}
            className="bg-gray-600 hover:bg-gray-700 px-6 py-2 rounded text-white"
          >
            Reset
          </button>
        </div>
      </form>
    </div>
  );
};

export default EmployeeForm;
