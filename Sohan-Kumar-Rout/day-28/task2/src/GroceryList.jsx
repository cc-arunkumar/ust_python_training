import React from "react";
import "./App.css";

const GroceryList = ({ items, addToCart }) => {
  return (
    <div className="grocery-container">
      <h2>Available Groceries</h2>

      {items.map((item) => (
        <div
          key={item.id}
          className={`grocery-item ${item.price > 50 ? "expensive" : ""}`}
        >
          <span>
            {item.name} - ₹{item.price}
          </span>

          <button className="add-btn" onClick={() => addToCart(item)}>
            Add to Cart
          </button>
        </div>
      ))}
    </div>
  );
};

export default GroceryList;
