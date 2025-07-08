import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add request interceptor to include auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  login: (credentials) => api.post('/auth/login', credentials),
  register: (userData) => api.post('/auth/register', userData),
  adminLogin: (credentials) => api.post('/auth/admin/login', credentials),
};

// Customer API
export const customerAPI = {
  getProfile: () => api.get('/customers/me'),
  updateProfile: (data) => api.put('/customers/me', data),
  getCustomers: () => api.get('/customers'),
};

// User API (alias for customer API for consistency)
export const userAPI = {
  getProfile: () => api.get('/customers/me'),
  updateProfile: (data) => api.put('/customers/me', data),
};

// Product API
export const productAPI = {
  getProducts: (params = {}) => api.get('/products', { params }),
  getProduct: (id) => api.get(`/products/${id}`),
  createProduct: (data) => api.post('/products', data),
  updateProduct: (id, data) => api.put(`/products/${id}`, data),
  deleteProduct: (id) => api.delete(`/products/${id}`),
};

// Order API
export const orderAPI = {
  getOrders: () => api.get('/orders'),
  createOrder: (data) => api.post('/orders', data),
  updateOrder: (id, data) => api.put(`/orders/${id}`, data),
};

// Cart API
export const cartAPI = {
  getCart: () => api.get('/cart'),
  addToCart: (data) => api.post('/cart', data),
  updateCart: (id, data) => api.put(`/cart/${id}`, data),
  removeFromCart: (id) => api.delete(`/cart/${id}`),
  clearCart: () => api.delete('/cart'),
};

// Analytics API
export const analyticsAPI = {
  getTopCustomers: (limit = 3) => api.get(`/analytics/top-customers?limit=${limit}`),
  getDailyOrders: () => api.get('/analytics/daily-orders'),
  getDeliveryRatings: () => api.get('/analytics/delivery-ratings'),
  getPopularProducts: (limit = 5) => api.get(`/analytics/popular-products?limit=${limit}`),
};

// Supplier API
export const supplierAPI = {
  getSuppliers: () => api.get('/suppliers'),
  createSupplier: (data) => api.post('/suppliers', data),
};

// Delivery Man API
export const deliveryManAPI = {
  getDeliveryMen: () => api.get('/delivery-men'),
  createDeliveryMan: (data) => api.post('/delivery-men', data),
};

// Review API
export const reviewAPI = {
  getReviews: (deliveryManId) => 
    api.get('/reviews', { params: deliveryManId ? { delivery_man_id: deliveryManId } : {} }),
  createReview: (data) => api.post('/reviews', data),
};

export default api;
