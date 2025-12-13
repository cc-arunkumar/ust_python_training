import React, { useState } from "react";
import GroceryList from "./GroceryList";
import Cart from "./Cart";
import "./App.css";

const App = () => {
  const groceryItems = [
    { id: 1, name: "Rice", price: 50 },
    { id: 2, name: "Wheat", price: 40 },
    { id: 3, name: "Tomatoes", price: 30 },
    { id: 4, name: "Milk", price: 20 },
    { id: 5, name: "Potatoes", price: 25 },
  ];

  const [cartItems, setCartItems] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [sortBy, setSortBy] = useState("default");
  const [cartPulse, setCartPulse] = useState(false);
  const [totalPrice, setTotalPrice] = useState(0);
  const [discountApplied, setDiscountApplied] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const handleAddToCart = (item) => {
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
    // small cart pulse to draw attention
    setCartPulse(true);
    setTimeout(() => setCartPulse(false), 700);
    setTimeout(() => setSuccessMessage(""), 2000);
  };

  const handleRemoveFromCart = (itemId) => {
    setCartItems(cartItems.filter((item) => item.id !== itemId));
  };

  const handleChangeQuantity = (itemId, newQuantity) => {
    if (newQuantity <= 0) return;
    setCartItems(
      cartItems.map((item) =>
        item.id === itemId ? { ...item, quantity: newQuantity } : item
      )
    );
  };

  const calculateTotal = () => {
    const total = cartItems.reduce(
      (acc, item) => acc + item.price * item.quantity,
      0
    );
    setTotalPrice(total);
    setDiscountApplied(total > 1000);
  };

  React.useEffect(() => {
    calculateTotal();
    // persist cart to localStorage
    try {
      localStorage.setItem("cart:v1", JSON.stringify(cartItems));
    } catch (e) {
      // ignore storage errors
    }
  }, [cartItems]);

  // load cart from localStorage on mount
  React.useEffect(() => {
    try {
      const raw = localStorage.getItem("cart:v1");
      if (raw) {
        setCartItems(JSON.parse(raw));
      }
    } catch (e) {
      // ignore
    }
  }, []);

  const dynamicBgColor = totalPrice > 1000 ? "#f7fff5" : "#fbfcfe"; // subtle change
  const dynamicDiscountStyle = discountApplied
    ? { color: "#ff6b6b", fontWeight: "bold" }
    : {};

  const handleClearCart = () => {
    setCartItems([]);
    setSuccessMessage("Cart cleared");
    setTimeout(() => setSuccessMessage(""), 1800);
  };

  const handleCheckout = () => {
    if (cartItems.length === 0) return;
    // simulate checkout
    setSuccessMessage("Order placed successfully! 🎉");
    setCartItems([]);
    setTimeout(() => setSuccessMessage(""), 2200);
  };

  const totalItems = cartItems.reduce((s, i) => s + (i.quantity || 0), 0);

  const filteredItems = groceryItems
    .filter((i) =>
      i.name.toLowerCase().includes(searchTerm.trim().toLowerCase())
    )
    .sort((a, b) => {
      if (sortBy === "price-asc") return a.price - b.price;
      if (sortBy === "price-desc") return b.price - a.price;
      return a.id - b.id;
    });

  const [theme, setTheme] = useState("light");

  const toggleTheme = () => setTheme((t) => (t === "light" ? "dark" : "light"));

  return (
    <div
      className="app"
      data-theme={theme}
      style={{ backgroundColor: dynamicBgColor }}
    >
      <div className="content">
        <div className="topbar">
          <div className="brand">
            <div className={`logo-circle ${cartPulse ? "pulse" : ""}`}>
              {totalItems > 0 ? totalItems : "KS"}
            </div>
            <h1>Kunil Super Market</h1>
          </div>
          <div className="controls">
            <input
              className="search"
              placeholder="Search groceries..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              aria-label="Search groceries"
            />
            <select
              className="sort"
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              aria-label="Sort groceries"
            >
              <option value="default">Sort</option>
              <option value="price-asc">Price: Low → High</option>
              <option value="price-desc">Price: High → Low</option>
            </select>
            <button
              className="btn ghost"
              onClick={toggleTheme}
              aria-label="Toggle theme"
            >
              {theme === "light" ? "Dark" : "Light"}
            </button>
          </div>
        </div>

        <div className="hero">
          <div className="hero-title">Fresh groceries, delivered with care</div>
          <div className="hero-sub">
            Clean, fast, and friendly shopping — add items on the left, review
            your cart on the right.
          </div>
        </div>

        <div className="layout">
          <GroceryList items={filteredItems} onAddToCart={handleAddToCart} />
          <Cart
            cartItems={cartItems}
            onRemoveFromCart={handleRemoveFromCart}
            onChangeQuantity={handleChangeQuantity}
            totalPrice={totalPrice}
            discountApplied={discountApplied}
            dynamicDiscountStyle={dynamicDiscountStyle}
            onClearCart={handleClearCart}
            onCheckout={handleCheckout}
            totalItems={totalItems}
          />
        </div>

        {successMessage && (
          <div className="success-message" role="status" aria-live="polite">
            {successMessage}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
