import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [emp_id, setEmpId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("http://localhost:8000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ emp_id, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Invalid credentials");
      }

      // Save to localStorage
      localStorage.setItem("token", data.access_token || data.token);
      localStorage.setItem("emp_id", data.emp_id);
      localStorage.setItem("user_name", data.name || "Manager");
      localStorage.setItem("role", data.role);

      // Redirect based on role
      if (data.role === "Manager") {
        navigate("/manager/dashboard");
      } else if (data.role === "Admin") {
        navigate("/admin/employees");
      } else if (data.role === "Employee") {
        navigate("/employee/tasks");
      } else {
        navigate("/login");
      }
    } catch (err) {
      console.error("Login error:", err);
      setError(err.message || "Login failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-blue-500">
      <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-800">
          Member Login
        </h2>

        {error && (
          <div className="mb-4 text-red-500 text-sm text-center">{error}</div>
        )}

        <form onSubmit={handleLogin} className="space-y-4">
          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">🆔</span>
            <input
              type="text"
              placeholder="Employee ID"
              value={emp_id}
              onChange={(e) => setEmpId(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
          </div>

          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">🔒</span>
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full bg-green-500 hover:bg-green-600 text-white py-2 rounded font-semibold"
          >
            LOGIN
          </button>

          <div className="text-center text-sm mt-2">
            <a href="#" className="text-blue-600 hover:underline">
              Forgot Employee ID / Password?
            </a>
          </div>

          <div className="text-center text-sm mt-4">
            <a href="#" className="text-blue-600 hover:underline">
              Create your Account →
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
