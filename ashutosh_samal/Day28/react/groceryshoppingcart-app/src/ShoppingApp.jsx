import React, { useState } from 'react';
import GroceryList from './GroceryList';
import Cart from './Cart';

const ShoppingApp = () => {
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
  const [successMessage, setSuccessMessage] = useState('');

  const handleAddToCart = (item) => {
    const existingItemIndex = cartItems.findIndex(cartItem => cartItem.id === item.id);
    if (existingItemIndex >= 0) {
      const updatedCartItems = [...cartItems];
      updatedCartItems[existingItemIndex].quantity += 1;
      setCartItems(updatedCartItems);
    } else {
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
    }
    calculateTotalPrice();
    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(''), 3000);
  };

  const handleRemoveFromCart = (itemId) => {
    const updatedCartItems = cartItems.filter(item => item.id !== itemId);
    setCartItems(updatedCartItems);
    calculateTotalPrice();
  };

  const handleChangeQuantity = (itemId, quantity) => {
    const updatedCartItems = cartItems.map(item => 
      item.id === itemId ? { ...item, quantity } : item
    );
    setCartItems(updatedCartItems);
    calculateTotalPrice();
  };

  const calculateTotalPrice = () => {
    let total = 0;
    cartItems.forEach(item => {
      total += item.price * item.quantity;
    });
    if (total > 1000 && !discountApplied) {
      setTotalPrice(total * 0.9);
      setDiscountApplied(true);
    } else {
      setTotalPrice(total);
      setDiscountApplied(false);
    }
  };

  return (
    <div>
      <h1>LULU Hypermart</h1>
      {successMessage && <p>{successMessage}</p>}
      <GroceryList groceryItems={groceryItems} onAddToCart={handleAddToCart} />
      <Cart
        cartItems={cartItems}
        onRemoveFromCart={handleRemoveFromCart}
        onChangeQuantity={handleChangeQuantity}
        totalPrice={totalPrice}
        discountApplied={discountApplied}
      />
    </div>
  );
};

export default ShoppingApp;
