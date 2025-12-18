import { useEffect, useState } from "react";
import { loginByUser } from "../api/users";
import { useNavigate } from "react-router-dom"; 

export default function Login() {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem("token")) {
      navigate("/", { replace: true });
    }
  }, [navigate]);

  const handleLogin = async () => {
    setLoading(true);
    try {
      const data = await loginByUser(userId, password);
      localStorage.setItem("token", data.access_token); // always store token
      navigate("/", { replace: true });
    } catch {
      alert("Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col md:flex-row h-screen">
      {/* Left branding panel */}
      <div className="flex-1 flex flex-col justify-center items-center bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 text-white p-10 relative overflow-hidden">
        <div className="absolute inset-0 bg-black opacity-20 mix-blend-multiply"></div>
        <h1 className="text-5xl font-extrabold mb-6 animate-fade-in">
          Jira Lite
        </h1>
        <p className="text-lg max-w-md text-center leading-relaxed animate-slide-up">
          A lightweight project management tool designed for speed, simplicity,
          and collaboration. Track tasks, manage sprints, and stay productive
          with a clean, intuitive interface.
        </p>
        <div className="absolute -bottom-20 -left-20 w-72 h-72 bg-purple-400 rounded-full opacity-30 blur-3xl animate-pulse"></div>
        <div className="absolute -top-20 -right-20 w-72 h-72 bg-indigo-400 rounded-full opacity-30 blur-3xl animate-pulse"></div>
      </div>

      {/* Right login form */}
      <div className="flex-1 flex items-center justify-center bg-gray-50">
        <div className="bg-white shadow-xl rounded-lg p-8 w-96 animate-slide-up">
          <h2 className="text-2xl font-bold text-center text-gray-800 mb-6">
            Login
          </h2>
          <div className="space-y-4">
            <input
              type="text"
              placeholder="User ID"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute inset-y-0 right-3 flex items-center text-sm text-indigo-600 hover:text-indigo-800"
              >
                {showPassword ? "Hide" : "Show"}
              </button>
            </div>
            <button
              onClick={handleLogin}
              disabled={loading}
              className="w-full bg-indigo-600 text-white py-3 rounded-lg hover:bg-indigo-700 transition-colors disabled:opacity-60"
            >
              {loading ? "Logging in..." : "Login"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
