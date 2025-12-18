import React, { useState } from "react";
import "./Login.css";

function Login({ setIsLoggedIn }) {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(""); // For error message handling

  const handleLogin = async () => {
    setError(""); // Clear previous errors

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/users/login/by-user?user_id=${userId}&password=${password}`,
        { method: "POST" }
      );

      if (!res.ok) {
        throw new Error("Invalid credentials");
      }

      const data = await res.json();
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("role", data.role); // Set role dynamically from backend
      localStorage.setItem("user_id", userId);

      // Directly navigate to Home (no need for an alert)
      setIsLoggedIn(true);
    } catch (err) {
      setError("Invalid User ID or Password"); // Show error if credentials are wrong
    }
  };

  return (
    <div className="login-wrapper">
      <div className="login-card">
        <h2>Login</h2>
        <p className="subtitle">Access your account</p>

        <div className="input-group">
          <input
            type="text"
            placeholder="User ID"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
          />
        </div>

        <div className="input-group">
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {error && <p className="error">{error}</p>} {/* Error message */}

        <button onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
}

export default Login;
