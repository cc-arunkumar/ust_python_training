import React, { useState } from "react";
import GroceryList from "./GroceryList"; // Importing GroceryList component
import Cart from "./Cart"; // Importing Cart component
import "./App.css"; // Importing CSS for styling

const App = () => {
  // Initial grocery items list with id, name, and price
  const groceryItems = [
    { id: 1, name: 'Rice', price: 50 },
    { id: 2, name: 'Wheat', price: 40 },
    { id: 3, name: 'Tomatoes', price: 30 },
    { id: 4, name: 'Milk', price: 20 },
    { id: 5, name: 'Potatoes', price: 25 },
  ];

  // State hooks for managing cart items, total price, discount flag, and success message
  const [cartItems, setCartItems] = useState([]); 
  const [totalPrice, setTotalPrice] = useState(0); 
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState(''); 

  // Function to handle adding items to the cart
  const handleAddToCart = (item) => {
    // Check if the item is already in the cart
    const existingItem = cartItems.find((cartItem) => cartItem.id === item.id);
    
    if (existingItem) {
      // If the item exists, update its quantity
      setCartItems(cartItems.map((cartItem) =>
        cartItem.id === item.id ? { ...cartItem, quantity: cartItem.quantity + 1 } : cartItem
      ));
    } else {
      // If the item is not in the cart, add it with quantity 1
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
    }
    
    // Display success message when an item is added to the cart
    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(''), 2000); // Hide the message after 2 seconds
  };

  // Function to handle removing items from the cart
  const handleRemoveFromCart = (itemId) => {
    // Filter out the item to remove it from the cart
    setCartItems(cartItems.filter((item) => item.id !== itemId));
  };

  // Function to handle updating the quantity of an item in the cart
  const handleChangeQuantity = (itemId, newQuantity) => {
    if (newQuantity <= 0) return; // Prevent setting quantity to zero or negative
    // Update the quantity of the item in the cart
    setCartItems(cartItems.map((item) =>
      item.id === itemId ? { ...item, quantity: newQuantity } : item
    ));
  };

  // Function to calculate the total price of items in the cart
  const calculateTotal = () => {
    // Sum the price of each item multiplied by its quantity
    const total = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
    setTotalPrice(total); // Set the total price
    setDiscountApplied(total > 1000); // Apply discount if total is greater than ₹1000
  };

  // Recalculate total price whenever cartItems change
  React.useEffect(() => {
    calculateTotal();
  }, [cartItems]); // Dependency array ensures this effect runs when cartItems change

  // Dynamically set the background color based on total price
  const dynamicBgColor = totalPrice > 1000 ? "#d3ffd3" : "#f4f4f9"; // Greenish if total > ₹1000
  // Apply a bold style for the discount if applied
  const dynamicDiscountStyle = discountApplied ? { color: "#ff5722", fontWeight: "bold" } : {};

  return (
    <div className="app" style={{ backgroundColor: dynamicBgColor }}>
      <h1>Sunku Market</h1>
      {/* Render the GroceryList component and pass the necessary props */}
      <GroceryList items={groceryItems} onAddToCart={handleAddToCart} />
      {/* Render the Cart component and pass the necessary props */}
      <Cart
        cartItems={cartItems}
        onRemoveFromCart={handleRemoveFromCart}
        onChangeQuantity={handleChangeQuantity}
        totalPrice={totalPrice}
        discountApplied={discountApplied}
        dynamicDiscountStyle={dynamicDiscountStyle}
      />
      {/* Display the success message if there's one */}
      {successMessage && <div className="success-message">{successMessage}</div>}
    </div>
  );
};

export default App;
