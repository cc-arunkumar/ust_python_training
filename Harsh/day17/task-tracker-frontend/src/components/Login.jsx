import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Login() {
  const { login } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [errorKey, setErrorKey] = useState(0); // used to re-trigger animation

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);
      setError("");
    } catch {
      setError("Invalid username or password");
      setErrorKey((prev) => prev + 1); // change key to restart animation
    }
  };

  return (
    <div className="login-container">
      <div className="login-left">
        <h1 className="brand-title">Task Tracker</h1>
        <p className="brand-subtitle">
          Organize your day, boost productivity, and never miss a task.
        </p>
      </div>

      <div className="login-right">
        <form onSubmit={handleSubmit} className="login-form">
          <h2>Welcome</h2>
          <p className="form-subtitle">
            Sign in to continue managing your tasks
          </p>

          {error && (
            <p key={errorKey} className="form-error animate-error">
              {error}
            </p>
          )}

          <div className="form-group">
            <label htmlFor="username" className="form-label">Username</label>
            <input
              id="username"
              className="input-field"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password" className="form-label">Password</label>
            <input
              id="password"
              type="password"
              className="input-field"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
            />
          </div>

          <button type="submit" className="btn-primary">Login</button>
        </form>
      </div>
    </div>
  );
}
