import React, { useState } from 'react';
import GroceryList from './GroceryList.jsx';
import Cart from './Cart.jsx';

import './App.css';

function App() {
  const [groceryItems, setGroceryItems] = useState([
    { id: 1, name: 'Rice', price: 50 },
    { id: 2, name: 'Wheat', price: 40 },
    { id: 3, name: 'Tomatoes', price: 30 },
    { id: 4, name: 'Milk', price: 20 },
    { id: 5, name: 'Potatoes', price: 25 },
  ]);
  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);

  // Add item to cart
  const addToCart = (item) => {
    const existingItem = cartItems.find(cartItem => cartItem.id === item.id);
    if (existingItem) {
      setCartItems(cartItems.map(cartItem => 
        cartItem.id === item.id ? { ...cartItem, quantity: cartItem.quantity + 1 } : cartItem
      ));
    } else {
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
    }
    calculateTotalPrice();
  };

  // Remove item from cart
  const removeFromCart = (id) => {
    const updatedCart = cartItems.filter(item => item.id !== id);
    setCartItems(updatedCart);
    calculateTotalPrice(updatedCart);
  };

  // Calculate the total price and apply discount
  const calculateTotalPrice = () => {
    let total = cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0);
    if (total > 1000 && !discountApplied) {
      setDiscountApplied(true);
      total = total - total * 0.1; // 10% discount
    }
    setTotalPrice(total);
  };

  // Update item quantity in the cart
  const updateQuantity = (id, newQuantity) => {
    setCartItems(cartItems.map(item => 
      item.id === id ? { ...item, quantity: newQuantity } : item
    ));
    calculateTotalPrice();
  };

  return (
    <div className="app">
      <h1>Grocery Shopping Cart</h1>
      <GroceryList groceryItems={groceryItems} addToCart={addToCart} />
      <Cart 
        cartItems={cartItems} 
        removeFromCart={removeFromCart} 
        updateQuantity={updateQuantity} 
        totalPrice={totalPrice} 
        discountApplied={discountApplied}
      />
    </div>
  );
}

export default App;
