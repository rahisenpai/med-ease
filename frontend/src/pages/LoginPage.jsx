import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Mail, Lock, User, AlertCircle } from 'lucide-react';

const LoginPage = () => {
  const [formData, setFormData] = useState({
    EmailID: '',
    Password: '',
  });
  const [isAdmin, setIsAdmin] = useState(false);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const { login, adminLogin } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    try {
      let result;
      if (isAdmin) {
        result = await adminLogin({
          Admin_Username: formData.EmailID,
          Admin_Password: formData.Password,
        });
      } else {
        result = await login(formData);
      }

      if (result.success) {
        navigate(isAdmin ? '/admin' : '/products');
      } else {
        setError(result.error);
      }
    } catch (err) {
      setError('An unexpected error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div className="card p-8">
          <div className="text-center">
            <User className="mx-auto h-12 w-12 text-blue-600" />
            <h2 className="mt-4 text-3xl font-bold text-gray-900">
              Sign in to MedEase
            </h2>
            <p className="mt-2 text-sm text-gray-600">
              Or{' '}
              <Link
                to="/register"
                className="font-medium text-blue-600 hover:text-blue-500"
              >
                create a new account
              </Link>
            </p>
          </div>

          <div className="mt-6">
            <div className="flex justify-center space-x-4 mb-6">
              <button
                type="button"
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  !isAdmin
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
                onClick={() => setIsAdmin(false)}
              >
                Customer Login
              </button>
              <button
                type="button"
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  isAdmin
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
                onClick={() => setIsAdmin(true)}
              >
                Admin Login
              </button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6">
              {error && (
                <div className="bg-red-50 border border-red-200 rounded-md p-4 flex items-center space-x-2">
                  <AlertCircle className="h-5 w-5 text-red-500" />
                  <span className="text-red-700">{error}</span>
                </div>
              )}

              <div>
                <label htmlFor="EmailID" className="block text-sm font-medium text-gray-700">
                  {isAdmin ? 'Username' : 'Email Address'}
                </label>
                <div className="mt-1 relative">
                  <input
                    id="EmailID"
                    name="EmailID"
                    type={isAdmin ? 'text' : 'email'}
                    required
                    className="input-field pl-10"
                    placeholder={isAdmin ? 'Enter username' : 'Enter your email'}
                    value={formData.EmailID}
                    onChange={handleChange}
                  />
                  <Mail className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>

              <div>
                <label htmlFor="Password" className="block text-sm font-medium text-gray-700">
                  Password
                </label>
                <div className="mt-1 relative">
                  <input
                    id="Password"
                    name="Password"
                    type="password"
                    required
                    className="input-field pl-10"
                    placeholder="Enter your password"
                    value={formData.Password}
                    onChange={handleChange}
                  />
                  <Lock className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>

              <div>
                <button
                  type="submit"
                  disabled={isLoading}
                  className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isLoading ? 'Signing in...' : 'Sign in'}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
