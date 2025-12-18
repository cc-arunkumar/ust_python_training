import { useState } from "react";
import { login } from "../api/auth.api";
import toast from "react-hot-toast";

export default function Login() {
  const [eId, setEId] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const res = await login({
        e_id: Number(eId),
        password,
      });

      localStorage.setItem("token", res.data.access_token);
      toast.success("Login successful");
      window.location.href = "/dashboard";
    } catch {
      toast.error("Invalid credentials");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-blue-100">
      {/* Animated Card */}
      <div className="w-full max-w-sm animate-fade-slide">
        <form
          onSubmit={submit}
          className="bg-white rounded-xl shadow-xl px-8 py-10"
        >
          {/* Logo / Title */}
          <div className="text-center mb-8">
            <h1 className="text-2xl font-semibold text-gray-800">
              Task Manager
            </h1>
            <p className="text-sm text-gray-500 mt-1">
              Sign in to continue
            </p>
          </div>

          {/* Employee ID */}
          <div className="mb-4">
            <label className="block text-xs font-medium text-gray-500 mb-1">
              Employee ID
            </label>
            <input
              type="number"
              required
              value={eId}
              onChange={(e) => setEId(e.target.value)}
              className="w-full border rounded-md px-3 py-2 text-sm
                         focus:outline-none focus:ring-2 focus:ring-blue-500
                         transition"
              placeholder="Enter your employee ID"
            />
          </div>

          {/* Password */}
          <div className="mb-6">
            <label className="block text-xs font-medium text-gray-500 mb-1">
              Password
            </label>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border rounded-md px-3 py-2 text-sm
                         focus:outline-none focus:ring-2 focus:ring-blue-500
                         transition"
              placeholder="Enter your password"
            />
          </div>

          {/* Button */}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2.5 rounded-md text-sm font-medium
                       hover:bg-blue-700 active:scale-[0.98]
                       transition-all duration-150
                       disabled:opacity-60"
          >
            {loading ? "Signing in…" : "Sign In"}
          </button>
        </form>

        {/* Footer */}
        <p className="text-xs text-gray-400 text-center mt-6">
          © 2025 Task Management System
        </p>
      </div>

      {/* Custom animation */}
      <style>
        {`
          @keyframes fade-slide {
            0% {
              opacity: 0;
              transform: translateY(20px);
            }
            100% {
              opacity: 1;
              transform: translateY(0);
            }
          }
          .animate-fade-slide {
            animation: fade-slide 0.6s ease-out;
          }
        `}
      </style>
    </div>
  );
}
