import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Package, ShoppingCart, Star, TrendingUp } from 'lucide-react';

const HomePage = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="hero-gradient text-white py-20">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="text-5xl font-bold mb-6">
            Welcome to <span className="text-yellow-300">MedEase</span>
          </h1>
          <p className="text-xl mb-8 max-w-3xl mx-auto">
            Your trusted online pharmacy for all medical needs. Fast delivery, genuine products, 
            and excellent customer service - all in one place.
          </p>
          
          {!isAuthenticated ? (
            <div className="space-x-4">
              <Link to="/register" className="btn-primary">
                Get Started
              </Link>
              <Link to="/login" className="btn-secondary text-white border-2 border-white hover:bg-white hover:text-purple-600">
                Sign In
              </Link>
            </div>
          ) : (
            <div className="space-x-4">
              <Link to="/products" className="btn-primary">
                Browse Products
              </Link>
              <Link to="/cart" className="btn-secondary text-white border-2 border-white hover:bg-white hover:text-purple-600">
                View Cart
              </Link>
            </div>
          )}
        </div>
      </div>

      {/* Features Section */}
      <div className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Why Choose MedEase?</h2>
            <p className="text-xl text-gray-600">We provide the best online pharmacy experience</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="card p-8 text-center">
              <Package className="feature-icon" />
              <h3 className="text-xl font-bold text-gray-900 mb-4">Wide Selection</h3>
              <p className="text-gray-600">
                Comprehensive range of medicines and healthcare products from trusted suppliers.
              </p>
            </div>

            <div className="card p-8 text-center">
              <ShoppingCart className="feature-icon" />
              <h3 className="text-xl font-bold text-gray-900 mb-4">Easy Ordering</h3>
              <p className="text-gray-600">
                Simple and intuitive ordering process with secure payment options.
              </p>
            </div>

            <div className="card p-8 text-center">
              <TrendingUp className="feature-icon" />
              <h3 className="text-xl font-bold text-gray-900 mb-4">Fast Delivery</h3>
              <p className="text-gray-600">
                Quick and reliable delivery service with real-time tracking.
              </p>
            </div>

            <div className="card p-8 text-center">
              <Star className="feature-icon" />
              <h3 className="text-xl font-bold text-gray-900 mb-4">Quality Service</h3>
              <p className="text-gray-600">
                Excellent customer service with loyalty rewards program.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Stats Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-16">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
            <div>
              <div className="text-5xl font-bold mb-2">10,000+</div>
              <div className="text-xl opacity-90">Happy Customers</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">5,000+</div>
              <div className="text-xl opacity-90">Products Available</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">24/7</div>
              <div className="text-xl opacity-90">Customer Support</div>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="py-20 px-4">
        <div className="max-w-4xl mx-auto">
          <div className="card p-12 text-center">
            <h2 className="text-4xl font-bold text-gray-900 mb-6">
              Ready to Experience Better Healthcare?
            </h2>
            <p className="text-xl text-gray-600 mb-8">
              Join thousands of satisfied customers who trust MedEase for their medical needs.
            </p>
            {!isAuthenticated && (
              <Link to="/register" className="btn-primary">
                Create Your Account Today
              </Link>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
