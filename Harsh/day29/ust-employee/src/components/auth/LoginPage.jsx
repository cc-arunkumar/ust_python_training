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
    setLoading(true);

    try {
      await login(email, password);
      setError('');
    } catch (err) {
      setError('Invalid credentials');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex">
      {/* Left side - Info */}
      <div className="hidden md:flex w-1/2 bg-gradient-to-br from-blue-600 to-indigo-600 text-white p-16 flex-col justify-center">
        <h1 className="text-5xl font-bold mb-6"> TaskPro</h1>
        <p className="text-lg mb-4">
          Manage your tasks efficiently, collaborate with your team, and track progress easily.
        </p>
        <ul className="list-disc list-inside space-y-2">
          <li>Organize tasks with ease</li>
          <li>Real-time collaboration</li>
          <li>Track deadlines and priorities</li>
          <li>Clean and intuitive interface</li>
        </ul>
      </div>

      {/* Right side - Login */}
      <div className="flex w-full md:w-1/2 items-center justify-center bg-white p-8">
        <div className="w-full max-w-md bg-white/80 backdrop-blur-xl rounded-2xl shadow-xl border border-gray-200 p-8">
          
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Task Manager
            </h1>
            <p className="text-gray-500 mt-2">Welcome back! Please login</p>
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
              <label className="block text-sm font-medium text-gray-600 mb-2">Email Address</label>
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
              <label className="block text-sm font-medium text-gray-600 mb-2">Password</label>
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
              {loading ? 'Signing in...' : 'Sign In'}
            </button>
          </form>

          {/* Footer */}
          <p className="text-center text-sm text-gray-400 mt-8">© 2025 Task Manager</p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
