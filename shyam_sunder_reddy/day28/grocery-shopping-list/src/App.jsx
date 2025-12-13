import { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css"; // import styles

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
    setTimeout(() => setSuccessMessage(""), 2000);
  };

  const removeFromCart = (id) => {
    setCartItems(cartItems.filter((item) => item.id !== id));
  };

  const updateQuantity = (id, quantity) => {
    if (quantity <= 0) {
      removeFromCart(id);
    } else {
      setCartItems(
        cartItems.map((item) =>
          item.id === id ? { ...item, quantity: quantity } : item
        )
      );
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">🛒 Grocery Shopping Cart</h1>
      {successMessage && <p className="success">{successMessage}</p>}

      <div className="layout">
        <GroceryList items={groceryItems} addToCart={addToCart} />
        <Cart
          cartItems={cartItems}
          removeFromCart={removeFromCart}
          updateQuantity={updateQuantity}
        />
      </div>
    </div>
  );
}

export default App;
