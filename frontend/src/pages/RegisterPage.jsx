import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Mail, Lock, User, Phone, MapPin, Calendar, AlertCircle } from 'lucide-react';

const RegisterPage = () => {
  const [formData, setFormData] = useState({
    FirstName: '',
    LastName: '',
    EmailID: '',
    Password: '',
    PhoneNumber: '',
    Address: '',
    Name: '',
    Pincode: '',
  });
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const { register } = useAuth();
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
      // Auto-generate Name field from FirstName and LastName
      const registrationData = {
        ...formData,
        Name: `${formData.FirstName} ${formData.LastName}`.trim()
      };
      
      const result = await register(registrationData);
      if (result.success) {
        navigate('/login');
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
      <div className="max-w-2xl w-full space-y-8">
        <div className="card p-8">
          <div className="text-center">
            <User className="mx-auto h-12 w-12 text-blue-600" />
            <h2 className="mt-4 text-3xl font-bold text-gray-900">
              Create your account
            </h2>
            <p className="mt-2 text-sm text-gray-600">
              Or{' '}
              <Link
                to="/login"
                className="font-medium text-blue-600 hover:text-blue-500"
              >
                sign in to your existing account
              </Link>
            </p>
          </div>

          <form onSubmit={handleSubmit} className="mt-8 space-y-6">
            {error && (
              <div className="bg-red-50 border border-red-200 rounded-md p-4 flex items-center space-x-2">
                <AlertCircle className="h-5 w-5 text-red-500" />
                <span className="text-red-700">{error}</span>
              </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label htmlFor="FirstName" className="block text-sm font-medium text-gray-700">
                  First Name
                </label>
                <div className="mt-1 relative">
                  <input
                    id="FirstName"
                    name="FirstName"
                    type="text"
                    required
                    className="input-field pl-10"
                    placeholder="Enter your first name"
                    value={formData.FirstName}
                    onChange={handleChange}
                  />
                  <User className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>

              <div>
                <label htmlFor="LastName" className="block text-sm font-medium text-gray-700">
                  Last Name
                </label>
                <div className="mt-1 relative">
                  <input
                    id="LastName"
                    name="LastName"
                    type="text"
                    required
                    className="input-field pl-10"
                    placeholder="Enter your last name"
                    value={formData.LastName}
                    onChange={handleChange}
                  />
                  <User className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>

              <div>
                <label htmlFor="EmailID" className="block text-sm font-medium text-gray-700">
                  Email Address
                </label>
                <div className="mt-1 relative">
                  <input
                    id="EmailID"
                    name="EmailID"
                    type="email"
                    required
                    className="input-field pl-10"
                    placeholder="Enter your email"
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
                <label htmlFor="PhoneNumber" className="block text-sm font-medium text-gray-700">
                  Phone Number
                </label>
                <div className="mt-1 relative">
                  <input
                    id="PhoneNumber"
                    name="PhoneNumber"
                    type="tel"
                    className="input-field pl-10"
                    placeholder="Enter your phone number"
                    value={formData.PhoneNumber}
                    onChange={handleChange}
                  />
                  <Phone className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>

              <div>
                <label htmlFor="Pincode" className="block text-sm font-medium text-gray-700">
                  Pincode
                </label>
                <div className="mt-1 relative">
                  <input
                    id="Pincode"
                    name="Pincode"
                    type="text"
                    className="input-field pl-10"
                    placeholder="Enter your pincode"
                    value={formData.Pincode}
                    onChange={handleChange}
                  />
                  <MapPin className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
                </div>
              </div>
            </div>

            <div>
              <label htmlFor="Address" className="block text-sm font-medium text-gray-700">
                Address
              </label>
              <div className="mt-1 relative">
                <textarea
                  id="Address"
                  name="Address"
                  rows={3}
                  className="input-field pl-10"
                  placeholder="Enter your address"
                  value={formData.Address}
                  onChange={handleChange}
                />
                <MapPin className="h-5 w-5 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>

            <div>
              <button
                type="submit"
                disabled={isLoading}
                className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isLoading ? 'Creating Account...' : 'Create Account'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
