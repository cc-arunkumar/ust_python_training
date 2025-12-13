import { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css";

export default function App() {
  const [cartItems, setCartItems] = useState([]);
  const [successMessage, setSuccessMessage] = useState("");

  const addToCart = (item) => {
    const existingItem = cartItems.find((cartItem) => cartItem.id === item.id);

    if (existingItem) {
      setCartItems(
        cartItems.map((cartItem) =>
          cartItem.id === item.id
            ? { ...cartItem, quantity: cartItem.quantity + 1 }
            : cartItem
        )
      );
    } else {
      setCartItems([...cartItems, { ...item, quantity: 1 }]);
    }

    setSuccessMessage(`${item.name} added to cart!`);
    setTimeout(() => setSuccessMessage(""), 3000);
  };

  const removeFromCart = (itemId) => {
    setCartItems(cartItems.filter((item) => item.id !== itemId));
  };

  const updateQuantity = (itemId, newQuantity) => {
    if (newQuantity <= 0) {
      removeFromCart(itemId);
    } else {
      setCartItems(
        cartItems.map((item) =>
          item.id === itemId ? { ...item, quantity: newQuantity } : item
        )
      );
    }
  };

  const totalPrice = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );
  const discountApplied = totalPrice > 1000;

  return (
    <div className="app">
      <header className="app-header">
        <h1>🛒 Grocery Shopping Cart</h1>
      </header>

      {successMessage && (
        <div className="success-message">✓ {successMessage}</div>
      )}

      <div className="app-container">
        <GroceryList onAddToCart={addToCart} />
        <Cart
          cartItems={cartItems}
          onRemoveItem={removeFromCart}
          onUpdateQuantity={updateQuantity}
          totalPrice={totalPrice}
          discount={discountApplied}
        />
      </div>
    </div>
  );
}
