import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify"; // Import toast and ToastContainer
import "react-toastify/dist/ReactToastify.css"; // Import Toastify styles

const AuthPage = () => {
  const [emp_id, setEmpId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLogin, setIsLogin] = useState(true); // Toggle between login and signup forms
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(""); // Clear previous error messages

    if (!emp_id || !password) {
      setError("Please fill in both fields.");
      toast.error("Please fill in both fields."); // Show error notification
      return;
    }

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

      // Success toast
      toast.success("Login successful!");

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
      toast.error(err.message || "Login failed"); // Show error notification
    }
  };

  const handleSignup = async (e) => {
    // Handle signup logic here, similar to the login
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600">
      <div className="flex w-full max-w-screen-lg shadow-xl rounded-lg">
        {/* Left Side - Application Name */}
        <div className="w-1/2 bg-purple-700 text-white flex items-center justify-center rounded-l-lg">
          <h1 className="text-5xl font-extrabold text-center">JIRA LITE</h1>
        </div>

        {/* Right Side - Login/Signup Forms */}
        <div className="w-1/2 bg-white p-8 rounded-r-lg">
          <div className="text-center mb-6">
            <h2 className="text-3xl font-semibold text-gray-800">
              {isLogin ? "Welcome Back!" : "Create Your Account!"}
            </h2>
            <p className="text-gray-600 mt-2">
              {isLogin
                ? "Please log in to access your dashboard."
                : "Please sign up to create an account."}
            </p>
          </div>

          {error && (
            <div className="mb-4 text-red-500 text-sm text-center">
              {error}
            </div>
          )}

          <form onSubmit={isLogin ? handleLogin : handleSignup} className="space-y-6">
            <div className="relative">
              <input
                type="text"
                placeholder="Employee ID"
                value={emp_id}
                onChange={(e) => setEmpId(e.target.value)}
                className="w-full p-3 pl-12 pr-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                required
              />
              <span className="absolute left-4 top-3 text-gray-400">🆔</span>
            </div>

            <div className="relative">
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full p-3 pl-12 pr-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                required
              />
              <span className="absolute left-4 top-3 text-gray-400">🔒</span>
            </div>

            <button
              type="submit"
              className="w-full bg-gradient-to-r from-green-400 to-blue-500 hover:bg-gradient-to-l text-white py-3 rounded-lg font-semibold transition-all duration-300"
            >
              {isLogin ? "Login" : "Sign Up"}
            </button>

            <div className="text-center text-sm mt-3">
              <a href="#" className="text-blue-600 hover:underline">
                {isLogin ? "Forgot Employee ID / Password?" : "Already have an account? Login →"}
              </a>
            </div>
          </form>

          <div className="text-center mt-4">
            <button
              className="text-blue-600 hover:underline"
              onClick={() => setIsLogin(!isLogin)}
            >
              {isLogin
                ? "Don't have an account? Sign up here"
                : "Already have an account? Log in here"}
            </button>
          </div>
        </div>
      </div>

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default AuthPage;
