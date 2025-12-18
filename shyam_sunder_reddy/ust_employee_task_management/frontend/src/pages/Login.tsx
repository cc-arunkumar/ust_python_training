import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LogIn, Loader } from 'lucide-react';

const Login = () => {
  const [e_id, setE_id] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      console.log('🔐 Attempting login for e_id:', e_id);
      await login({ e_id: parseInt(e_id), password });
      console.log('✅ Login successful, redirecting...');
      navigate('/');
    } catch (err: any) {
      console.error('❌ Login error:', err);
      const errorMessage = err.response?.data?.detail || err.message || 'Invalid credentials. Please try again.';
      console.error('Error details:', {
        status: err.response?.status,
        data: err.response?.data,
        message: err.message,
      });
      setError(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <div className="w-full max-w-md animate-scale-in">
        <div className="card">
          <div className="text-center mb-8">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-primary-500 to-purple-500 rounded-2xl mb-4">
              <LogIn className="text-white" size={32} />
            </div>
            <h1 className="text-3xl font-bold text-gray-800 mb-2">Welcome Back</h1>
            <p className="text-gray-600">Sign in to your UST Task Management account</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg animate-slide-down">
                {error}
              </div>
            )}

            <div>
              <label htmlFor="e_id" className="block text-sm font-medium text-gray-700 mb-2">
                Employee ID
              </label>
              <input
                id="e_id"
                type="number"
                value={e_id}
                onChange={(e) => setE_id(e.target.value)}
                className="input-field"
                placeholder="Enter your employee ID"
                required
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
                Password
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field"
                placeholder="Enter your password"
                required
              />
            </div>

            <button
              type="submit"
              disabled={isLoading}
              className="w-full btn-primary flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? (
                <>
                  <Loader className="animate-spin" size={20} />
                  Signing in...
                </>
              ) : (
                <>
                  <LogIn size={20} />
                  Sign In
                </>
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;

