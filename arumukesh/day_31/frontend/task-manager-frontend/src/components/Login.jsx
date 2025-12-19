import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Login() {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState(null);
  const nav = useNavigate();
  const { login } = useAuth();

  const submit = async (e) => {
    e.preventDefault();
    try {
      await login(userId, password);
      nav("/dashboard");
    } catch (e) {
      console.error(e);
      setErr("Login failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form onSubmit={submit} className="w-96 bg-white p-8 rounded shadow">
        <h2 className="text-2xl font-semibold mb-4">Sign in to TaskFlow</h2>
        {err && <div className="text-red-600 mb-2">{err}</div>}
        <label className="block mb-2">Employee ID</label>
        <input
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          className="w-full p-2 border rounded mb-4"
        />
        <label className="block mb-2">Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded mb-6"
        />
        <button
          type="submit"
          className="w-full py-2 bg-[var(--accent)] text-white rounded"
        >
          Sign in
        </button>
      </form>
    </div>
  );
}
