import React from "react";
import "./App.css";

function GroceryList({ groceryItems, addToCart }) {
  return (
    <div className="grocery-list">
      <h2>Available Groceries</h2>
      <div className="card-container">
        {groceryItems.map((item) => (
          <div key={item.id} className="card">
            <img src={item.imageUrl} alt={item.name} />
            <h3>{item.name}</h3>
            <p>₹{item.price}</p>
            <button onClick={() => addToCart(item)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default GroceryList;
