import React, { useState } from "react";
import { login } from "../services/employeeService";

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await login(email, password);
      localStorage.setItem("token", res.token);
      onLogin();
    } catch (err) {
      setError("Invalid email or password");
    }
  };

  return (
    <div className="h-screen flex justify-center items-center bg-[#1C2333] px-4">
      <div className="bg-[#242C3B] p-10 rounded-xl shadow-xl w-full max-w-md text-white">
        <h2 className="text-3xl font-bold mb-6 text-center text-blue-400">
          Admin Login
        </h2>

        {error && (
          <p className="text-red-400 mb-4 text-center text-sm">{error}</p>
        )}

        <form onSubmit={handleSubmit}>
          {/* Email */}
          <label className="block mb-1 text-sm font-medium">Email</label>
          <input
            type="email"
            className="w-full p-3 mb-4 bg-[#1A2230] border border-[#2F3A4D] 
            rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 
            outline-none text-gray-200"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="block mb-1 text-sm font-medium">Password</label>
          <input
            type="password"
            className="w-full p-3 mb-6 bg-[#1A2230] border border-[#2F3A4D] 
            rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 
            outline-none text-gray-200"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            className="w-full bg-blue-600 py-3 rounded-lg font-semibold 
            hover:bg-blue-700 transition text-white"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
