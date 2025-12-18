import React, { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
 
function App() {
  const groceryItems = [
    { id: 1, name: "Rice", price: 50 },
    { id: 2, name: "Wheat", price: 40 },
    { id: 3, name: "Tomatoes", price: 30 },
    { id: 4, name: "Milk", price: 20 },
    { id: 5, name: "Potatoes", price: 25 },
  ];
 
  const [cartItems, setCartItems] = useState([]);
  const [successMessage, setSuccessMessage] = useState("");
 
  const addToCart = (item) => {
    setCartItems((prev) => {
      const existingItem = prev.find((i) => i.id === item.id);
 
      if (existingItem) {
        return prev.map((i) =>
          i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
        );
      } else {
        return [...prev, { ...item, quantity: 1 }];
      }
    });
 
    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(""), 2000);
  };
 
  const removeFromCart = (id) => {
    setCartItems(cartItems.filter((item) => item.id !== id));
  };
 
  const updateQuantity = (id, quantity) => {
    if (quantity <= 0) return;
 
    setCartItems(
      cartItems.map((item) =>
        item.id === id ? { ...item, quantity } : item
      )
    );
  };
 
  return (
    <div className="main_body" style={{ padding: "20px" }}>
      <h1>UST Grocery Shopping Cart</h1>
 
      {successMessage && (
        <p style={{ color: "green" }}>{successMessage}</p>
      )}
 
      <GroceryList items={groceryItems} addToCart={addToCart} />
      <Cart
        cartItems={cartItems}
        removeFromCart={removeFromCart}
        updateQuantity={updateQuantity}
      />
    </div>
  );
}
 
export default App;
 
 