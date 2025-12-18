import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

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

      localStorage.setItem("token", data.access_token || data.token);
      localStorage.setItem("emp_id", data.emp_id);
      localStorage.setItem("user_name", data.name || "Manager");
      localStorage.setItem("role", data.role);

      toast.success("Login successful!");
      setTimeout(() => {
        if (data.role === "Manager") navigate("/manager/dashboard");
        else if (data.role === "Admin") navigate("/admin/employees");
        else if (data.role === "Employee") navigate("/employee/tasks");
        else navigate("/login");
      }, 1000);
    } catch (err) {
      console.error("Login error:", err);
      toast.error(err.message || "Login failed");
      setError(err.message || "Login failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="flex w-full max-w-5xl bg-white rounded-xl shadow-lg overflow-hidden">
        {/* Left side - login form */}
        <div className="w-1/2 p-10">
          <div className="mb-6">
            <h2 className="text-3xl font-bold text-gray-800">Log in to your Account</h2>
            <p className="text-sm text-gray-500 mt-2">Welcome back! Select method to log in:</p>
          </div>

          {/* Social login buttons */}
          <div className="flex space-x-4 mb-6">
            <button className="flex-1 bg-red-500 text-white py-2 rounded hover:bg-red-600 transition">
              Google
            </button>
            <button className="flex-1 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition">
              Facebook
            </button>
          </div>

          {/* Separator */}
          <div className="flex items-center mb-6">
            <div className="flex-grow h-px bg-gray-300" />
            <span className="px-3 text-sm text-gray-500">or continue with email</span>
            <div className="flex-grow h-px bg-gray-300" />
          </div>

          {error && (
            <div className="mb-4 text-red-500 text-sm text-center">{error}</div>
          )}

          <form onSubmit={handleLogin} className="space-y-4">
            <input
              type="text"
              placeholder="Email ID"
              value={emp_id}
              onChange={(e) => setEmpId(e.target.value)}
              className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />

            <div className="flex items-center justify-between text-sm">
              <label className="flex items-center space-x-2">
                <input type="checkbox" className="form-checkbox" />
                <span>Remember me</span>
              </label>
              {/* <a href="#" className="text-purple-600 hover:underline">
                Forgot Password?
              </a> */}
            </div>

            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 text-white py-2 rounded font-semibold transition-all duration-300 shadow-md"
            >
              Log in
            </button>
          </form>

          {/* <p className="text-sm text-center mt-6 text-gray-600">
            Don't have an account?{" "}
            <a href="#" className="text-purple-600 font-medium hover:underline">
              Create an account
            </a>
          </p> */}
        </div>

        {/* Right side - illustration and promo */}
        <div className="w-1/2 bg-gradient-to-br from-indigo-500 to-purple-600 text-white flex flex-col justify-center items-center p-10">
          <div className="w-40 h-40 bg-white rounded-full mb-6 flex items-center justify-center text-indigo-600 font-bold text-2xl shadow-lg">
            JIRA LITE
          </div>
          <h3 className="text-xl font-semibold mb-2 text-center">
            Connect Employees and their task.
          </h3>
          <p className="text-sm text-center opacity-80">
            Good Morning Have a good day!.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
