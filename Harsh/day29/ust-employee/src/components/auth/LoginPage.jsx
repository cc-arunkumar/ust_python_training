import React, { useState } from 'react';
import { AlertCircle } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(email, password);
    } catch (err) {
      setError(err.message || 'Login failed. Please check your credentials.');
    } finally {
      setLoading(false);
    }
  };

  return (
  <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 p-4">
    <div className="w-full max-w-md bg-white/80 backdrop-blur-xl rounded-2xl shadow-xl border border-gray-200 p-8 transition-transform duration-300 hover:scale-[1.02]">
      
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
          Task Manager
        </h1>
        <p className="text-gray-500 mt-2">
          Welcome back! Please login
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        
        {/* Error */}
        {error && (
          <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded-lg flex items-center gap-2 animate-shake">
            <AlertCircle size={20} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        {/* Email */}
        <div>
          <label className="block text-sm font-medium text-gray-600 mb-2">
            Email Address
          </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@example.com"
            required
            className="w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 
                       focus:ring-2 focus:ring-blue-500 focus:border-transparent 
                       outline-none transition shadow-sm hover:shadow-md"
          />
        </div>

        {/* Password */}
        <div>
          <label className="block text-sm font-medium text-gray-600 mb-2">
            Password
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
            required
            className="w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 
                       focus:ring-2 focus:ring-blue-500 focus:border-transparent 
                       outline-none transition shadow-sm hover:shadow-md"
          />
        </div>

        {/* Button */}
        <button
          type="submit"
          disabled={loading}
          className="w-full py-3 rounded-xl font-semibold text-white
                     bg-gradient-to-r from-blue-600 to-indigo-600
                     hover:from-blue-700 hover:to-indigo-700
                     active:scale-95 transition-all duration-200
                     shadow-lg disabled:opacity-60 disabled:cursor-not-allowed"
        >
          {loading ? "Signing in..." : "Sign In"}
        </button>
      </form>

      {/* Footer */}
      <p className="text-center text-sm text-gray-400 mt-8">
        © 2025 Task Manager
      </p>
    </div>
  </div>
);

};

export default LoginPage;