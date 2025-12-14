import React, { useState, useEffect } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css";

const App = () => {
const [groceryItems] = useState([
  { id: 1, name: "Kurkure", price: 20, image: "https://i.imgur.com/7yUvePI.png" },
  { id: 2, name: "Apple", price: 40, image: "https://i.imgur.com/1bX5QH6.png" },
  { id: 3, name: "Munch", price: 20, image: "https://i.imgur.com/2yaf2wb.png" },
  { id: 4, name: "Milk", price: 20, image: "https://i.imgur.com/8zQZQYp.png" },
  { id: 5, name: "Handwash", price: 80, image: "https://i.imgur.com/0ZQZQYp.png" }
]);


  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const addToCart = (item) => {
    const exists = cartItems.find((cartItem) => cartItem.id === item.id);

    if (exists) {
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

    setTimeout(() => {
      setSuccessMessage("");
    }, 2000);
  };

  const removeFromCart = (id) => {
    setCartItems(cartItems.filter((item) => item.id !== id));
  };

  const updateQuantity = (id, quantity) => {
    setCartItems(
      cartItems.map((item) =>
        item.id === id ? { ...item, quantity: Number(quantity) } : item
      )
    );
  };

  useEffect(() => {
    let total = cartItems.reduce(
      (sum, item) => sum + item.price * item.quantity,
      0
    );

    if (total > 1000) {
      setDiscountApplied(true);
      total = total - total * 0.1;
    } else {
      setDiscountApplied(false);
    }

    setTotalPrice(total);
  }, [cartItems]);

  return (
    <div className="app-container">
      <marquee className="marquee-text" behavior="scroll" direction="left">
      Welcome to Lulu Supermart — Big Discounts Available Today!
      </marquee>

      <h1>Lulu Supermart</h1>

      {successMessage && (
        <div className={`success-message show`}>{successMessage}</div>
      )}

      <GroceryList items={groceryItems} addToCart={addToCart} />

      <Cart
        cartItems={cartItems}
        removeFromCart={removeFromCart}
        updateQuantity={updateQuantity}
        totalPrice={totalPrice}
        discountApplied={discountApplied}
      />
    </div>
  );
};

export default App;
