import { useEffect, useState } from "react";
import { loginByUser } from "../api/users";

export default function Login() {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token")) {
      window.location.href = "/";
    }
  }, []);

  const handleLogin = async () => {
    setLoading(true);
    try {
      const data = await loginByUser(userId, password);
      localStorage.setItem("token", data.access_token);
      window.location.href = "/";
    } catch {
      alert("Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen relative bg-white overflow-hidden">
      {/* Decorative background pattern in sidebar colors */}
      <div className="absolute inset-0">
        <svg
          className="absolute w-full h-full opacity-10 animate-pulse"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <pattern
              id="grid"
              width="40"
              height="40"
              patternUnits="userSpaceOnUse"
            >
              <path
                d="M 40 0 L 0 0 0 40"
                fill="none"
                stroke="#2b384bff"
                strokeWidth="0.5"
              />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid)" />
        </svg>

        {/* Gradient overlay with animation */}
        <div className="absolute inset-0 bg-gradient-to-br from-gray-100 via-gray-200 to-gray-300 opacity-30 animate-gradient"></div>

        {/* Floating circles */}
        <div className="absolute top-1/4 left-1/3 w-32 h-32 bg-gray-800 rounded-full opacity-10 animate-bounce-slow"></div>
        <div className="absolute bottom-1/4 right-1/4 w-24 h-24 bg-gray-900 rounded-full opacity-10 animate-bounce-slower"></div>

        {/* Welcome message in background */}
        <div className="absolute top-12 w-full text-center">
          <h1 className="text-4xl font-extrabold text-teal-800 opacity-20 tracking-wide animate-fade-in">
            Welcome to Jira Lite
          </h1>
        </div>
      </div>

      {/* Login card */}
      <div className="bg-white p-6 rounded-lg shadow-lg w-96 relative z-10">
        <h2 className="text-xl font-semibold mb-4 text-center text-gray-800">
          Login
        </h2>
        <div className="space-y-3">
          <input
            type="text"
            placeholder="User ID"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleLogin}
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition-colors disabled:opacity-60"
          >
            {loading ? "Logging in..." : "Login"}
          </button>
        </div>
      </div>
    </div>
  );
}
