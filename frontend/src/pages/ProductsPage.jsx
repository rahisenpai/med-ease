import React, { useState, useEffect } from 'react';
import { productAPI, cartAPI } from '../services/api';
import { Package, ShoppingCart, Plus, Minus } from 'lucide-react';

const ProductsPage = () => {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  const [cartItems, setCartItems] = useState({});

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setIsLoading(true);
      const response = await productAPI.getProducts();
      setProducts(response.data);
    } catch (err) {
      setError('Failed to fetch products');
    } finally {
      setIsLoading(false);
    }
  };

  const addToCart = async (product) => {
    try {
      await cartAPI.addToCart({
        ProductID: product.ProductID,
        Quantity: 1,
        Price: product.Price,
      });
      
      // Update local cart state
      setCartItems(prev => ({
        ...prev,
        [product.ProductID]: (prev[product.ProductID] || 0) + 1
      }));
      
      alert('Product added to cart!');
    } catch (err) {
      alert('Failed to add product to cart');
    }
  };

  const updateCartQuantity = (productId, quantity) => {
    if (quantity <= 0) {
      const newCartItems = { ...cartItems };
      delete newCartItems[productId];
      setCartItems(newCartItems);
    } else {
      setCartItems(prev => ({
        ...prev,
        [productId]: quantity
      }));
    }
  };

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-xl text-gray-600">Loading products...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-xl text-red-600">{error}</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Our Products</h1>
          <p className="text-lg text-gray-600">Browse our wide selection of medical products</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {products.map((product) => (
            <div key={product.ProductID} className="card p-6">
              <div className="flex items-center justify-center h-48 bg-gray-100 rounded-lg mb-4">
                <Package className="h-16 w-16 text-gray-400" />
              </div>
              
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {product.Name}
              </h3>
              
              <p className="text-sm text-gray-600 mb-3 line-clamp-3">
                {product.Description}
              </p>
              
              <div className="flex items-center justify-between mb-4">
                <span className="text-2xl font-bold text-blue-600">
                  ₹{product.Price}
                </span>
                <span className="text-sm text-gray-500">
                  {product.Quantity} in stock
                </span>
              </div>
              
              <div className="flex items-center justify-between mb-4">
                <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full">
                  {product.Category}
                </span>
              </div>

              {cartItems[product.ProductID] ? (
                <div className="flex items-center justify-between">
                  <button
                    onClick={() => updateCartQuantity(product.ProductID, cartItems[product.ProductID] - 1)}
                    className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300 transition-colors"
                  >
                    <Minus className="h-4 w-4" />
                  </button>
                  <span className="font-semibold text-lg">
                    {cartItems[product.ProductID]}
                  </span>
                  <button
                    onClick={() => updateCartQuantity(product.ProductID, cartItems[product.ProductID] + 1)}
                    className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300 transition-colors"
                  >
                    <Plus className="h-4 w-4" />
                  </button>
                </div>
              ) : (
                <button
                  onClick={() => addToCart(product)}
                  className="w-full btn-primary flex items-center justify-center space-x-2"
                  disabled={product.Quantity === 0}
                >
                  <ShoppingCart className="h-4 w-4" />
                  <span>{product.Quantity === 0 ? 'Out of Stock' : 'Add to Cart'}</span>
                </button>
              )}
            </div>
          ))}
        </div>

        {products.length === 0 && (
          <div className="text-center py-12">
            <Package className="h-16 w-16 text-gray-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-900 mb-2">No products found</h3>
            <p className="text-gray-600">Check back later for new products.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductsPage;
