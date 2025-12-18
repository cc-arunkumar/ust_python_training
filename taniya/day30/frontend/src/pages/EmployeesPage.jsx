import React, { useEffect, useState } from "react";
import { apiService } from "../services/api";
import "./EmployeesPage.css";

export default function EmployeesPage() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;
    async function load() {
      setLoading(true);
      setError(null);

      const token = apiService.getToken();
      const storedUser = JSON.parse(
        localStorage.getItem("taskflow_user") || "null"
      );
      const role =
        localStorage.getItem("taskflow_role") || storedUser?.roles?.[0];

      console.log("EmployeesPage: token:", token);
      console.log("EmployeesPage: role:", role);

      try {
        // call service with token so Authorization header is set
        const data = await apiService.getEmployees("", token);
        console.log("GET /employees response:", data);

        const list = Array.isArray(data) ? data : data?.employees || [];
        if (!mounted) return;
        setEmployees(list);
      } catch (err) {
        console.error("Failed to load employees:", err);
        if (!mounted) return;
        setError(err?.message || "Failed to load employees");
      } finally {
        if (mounted) setLoading(false);
      }
    }
    load();
    return () => {
      mounted = false;
    };
  }, []);

  if (loading) return <div>Loading employees…</div>;
  if (error) return <div className="tf-error">Error: {error}</div>;
  if (!employees.length) return <div>No employees found.</div>;

  return (
    <main className="employees-page">
      <h1>Employees</h1>
      <ul className="employees-list">
        {employees.map((e) => (
          <li key={e.id || e.emp_id}>
            <div>{e.name || e.full_name}</div>
            <div>{e.emp_id || e.id}</div>
            <div>{e.designation || e.title || "-"}</div>
          </li>
        ))}
      </ul>
    </main>
  );
}
