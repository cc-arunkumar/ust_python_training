import React, { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css";
 
const App = () => {
  const groceryItems = [
    { id: 1, name: 'Rice', price: 50 },
    { id: 2, name: 'Wheat', price: 40 },
    { id: 3, name: 'Tomatoes', price: 30 },
    { id: 4, name: 'Milk', price: 20 },
    { id: 5, name: 'Potatoes', price: 25 },
  ];
 
  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
 
  const handleAddToCart = (item) => {
    const existingItem = cartItems.find((cartItem) => cartItem.id === item.id);
    if (existingItem) {
      setCartItems(cartItems.map((cartItem) =>
        cartItem.id === item.id ? { ...cartItem, quantity: cartItem.quantity + 1 } : cartItem
      ));
    } else {
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
    }
    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(''), 2000);
  };
 
  const handleRemoveFromCart = (itemId) => {
    setCartItems(cartItems.filter((item) => item.id !== itemId));
  };
 
  const handleChangeQuantity = (itemId, newQuantity) => {
    if (newQuantity <= 0) return;
    setCartItems(cartItems.map((item) =>
      item.id === itemId ? { ...item, quantity: newQuantity } : item
    ));
  };
 
  const calculateTotal = () => {
    const total = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
    setTotalPrice(total);
    setDiscountApplied(total > 1000);
  };
 
  React.useEffect(() => {
    calculateTotal();
  }, [cartItems]);
 
  const dynamicBgColor = totalPrice > 1000 ? "#d3ffd3" : "#f4f4f9"; // Greenish if total > ₹1000
  const dynamicDiscountStyle = discountApplied ? { color: "#ff5722", fontWeight: "bold" } : {};
 
  return (
    <div className="app" style={{ backgroundColor: dynamicBgColor }}>
      <h1>Kunil Super Market</h1>
      <GroceryList items={groceryItems} onAddToCart={handleAddToCart} />
      <Cart
        cartItems={cartItems}
        onRemoveFromCart={handleRemoveFromCart}
        onChangeQuantity={handleChangeQuantity}
        totalPrice={totalPrice}
        discountApplied={discountApplied}
        dynamicDiscountStyle={dynamicDiscountStyle}
      />
      {successMessage && <div className="success-message">{successMessage}</div>}
    </div>
  );
};
 
export default App;
 