import React, { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css";

function App() {
  const [groceryItems, setGroceryItems] = useState([
    { id: 1, name: "Rice", price: 50 },
    { id: 2, name: "Wheat", price: 40 },
    { id: 3, name: "Tomatoes", price: 30 },
    { id: 4, name: "Milk", price: 20 },
    { id: 5, name: "Potatoes", price: 25 },
  ]);

  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const addToCart = (item) => {
    const updatedCart = [...cartItems];
    const existingItem = updatedCart.find((cartItem) => cartItem.id === item.id);
    
    if (existingItem) {
      existingItem.quantity += 1;
    } else {
      updatedCart.push({ ...item, quantity: 1 });
    }

    setCartItems(updatedCart);
    updateTotalPrice(updatedCart);
    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(""), 3000); // Hide message after 3 seconds
  };

  const removeFromCart = (id) => {
    const updatedCart = cartItems.filter((item) => item.id !== id);
    setCartItems(updatedCart);
    updateTotalPrice(updatedCart);
  };

  const updateQuantity = (id, quantity) => {
    const updatedCart = [...cartItems];
    const item = updatedCart.find((cartItem) => cartItem.id === id);
    if (item) {
      item.quantity = quantity;
    }
    setCartItems(updatedCart);
    updateTotalPrice(updatedCart);
  };

  const updateTotalPrice = (updatedCart) => {
    const total = updatedCart.reduce(
      (acc, item) => acc + item.price * item.quantity,
      0
    );
    setTotalPrice(total);

    if (total > 1000 && !discountApplied) {
      setDiscountApplied(true);
    } else if (total <= 1000 && discountApplied) {
      setDiscountApplied(false);
    }
  };

  return (
    <div className="App">
      <h1>Grocery Shopping Cart</h1>
      <GroceryList groceryItems={groceryItems} addToCart={addToCart} />
      <Cart
        cartItems={cartItems}
        removeFromCart={removeFromCart}
        updateQuantity={updateQuantity}
        totalPrice={totalPrice}
        discountApplied={discountApplied}
        successMessage={successMessage}
      />
    </div>
  );
}

export default App;
