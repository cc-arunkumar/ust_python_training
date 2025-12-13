import { useState ,useEffect} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {groceryItems} from "./data/GroceryData.jsx"
import GroceryList from './components/GroceryList.jsx'
import Cart from './components/Cart.jsx'
import SuccessMessage from './components/SuccessMessage.jsx'

export default function App() {
  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');

  // Calculate total price whenever cart changes
  useEffect(() => {
    const total = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    setTotalPrice(total);
    setDiscountApplied(total > 1000);
  }, [cartItems]);

  const handleAddToCart = (item) => {
    const existingItem = cartItems.find(cartItem => cartItem.id === item.id);
    
    if (existingItem) {
      setCartItems(cartItems.map(cartItem =>
        cartItem.id === item.id
          ? { ...cartItem, quantity: cartItem.quantity + 1 }
          : cartItem
      ));
      setSuccessMessage(`${item.name} quantity increased!`);
    } else {
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
      setSuccessMessage(`${item.name} added to cart!`);
    }
  };

  const handleUpdateQuantity = (itemId, newQuantity) => {
    if (newQuantity < 1) return;
    
    setCartItems(cartItems.map(item =>
      item.id === itemId
        ? { ...item, quantity: newQuantity }
        : item
    ));
  };

  const handleRemoveItem = (itemId) => {
    const item = cartItems.find(item => item.id === itemId);
    setCartItems(cartItems.filter(item => item.id !== itemId));
    setSuccessMessage(`${item.name} removed from cart!`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-orange-50">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            🛒 Grocery Shopping Cart
          </h1>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <GroceryList items={groceryItems} onAddToCart={handleAddToCart} />
          </div>
          
          <div className="lg:col-span-1">
            <div className="sticky top-4">
              <Cart
                cartItems={cartItems}
                onUpdateQuantity={handleUpdateQuantity}
                onRemoveItem={handleRemoveItem}
                totalPrice={totalPrice}
                discount={discountApplied}
              />
            </div>
          </div>
        </div>
      </div>

      {successMessage && (
        <SuccessMessage
          message={successMessage}
          onClose={() => setSuccessMessage('')}
        />
      )}

      <style jsx>{`
        @keyframes slide-in {
          from {
            transform: translateX(100%);
            opacity: 0;
          }
          to {
            transform: translateX(0);
            opacity: 1;
          }
        }
        .animate-slide-in {
          animation: slide-in 0.3s ease-out;
        }
      `}</style>
    </div>
  );
}