import { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { authService } from "../../services/authService";
import { toast } from "react-toastify";

const LoginPage = () => {
  const [empId, setEmpId] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!empId || !password) {
      toast.error("Please enter Employee ID and Password");
      return;
    }

    setLoading(true);
    try {
      // ✅ token is already a STRING
      const token = await authService.login(empId, password);

      // ✅ PASS TOKEN STRING DIRECTLY
      login(token);

      toast.success("Login successful!");
      navigate("/dashboard");
    } catch (err) {
      toast.error("Invalid credentials. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center login-hero">
      <div className="max-w-md w-full bg-white rounded-lg p-8 login-card">
        <h2 className="text-2xl text-center mb-2 login-brand">
          UST Task Manager
        </h2>
        <div className="login-accent" />

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Employee ID
            </label>
            <input
              type="text"
              value={empId}
              onChange={(e) => setEmpId(e.target.value)}
              className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md login-input"
              placeholder="e.g. 1"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md login-input"
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full text-white py-2 px-4 rounded-md login-button"
          >
            {loading ? "Signing in..." : "Login"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
