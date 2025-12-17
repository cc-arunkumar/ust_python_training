import React, { useState } from "react";
import { loginUser } from "../services/authService";

const Login = () => {
  const [emp_id, setEmpId] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await loginUser(emp_id, password);

      localStorage.setItem("token", res.access_token);
      localStorage.setItem("role", res.role);
      localStorage.setItem("emp_id", res.emp_id);

      if (res.role === "Admin") window.location.href = "/admin/employees";
      if (res.role === "Manager") window.location.href = "/manager/tasks";
      if (res.role === "Employee") window.location.href = "/employee/tasks";
    } catch (err) {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gray-900">
      <form
        onSubmit={handleLogin}
        className="bg-gray-800 p-8 rounded-xl text-white w-96"
      >
        <h2 className="text-2xl font-bold mb-6 text-blue-400">Login</h2>

        <input
          type="number"
          placeholder="Employee ID"
          value={emp_id}
          onChange={(e) => setEmpId(e.target.value)}
          className="w-full p-3 mb-4 bg-gray-700 rounded"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-3 mb-4 bg-gray-700 rounded"
        />

        <button className="w-full bg-blue-600 py-3 rounded hover:bg-blue-700">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
