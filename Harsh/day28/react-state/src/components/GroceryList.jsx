import React from "react";

const GroceryList = ({ items, addToCart }) => {
  return (
    <div className="grocery-list">
      <h2>Available Groceries</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id} className="grocery-item">
            <img src={item.image} alt={item.name} />
            <span>{item.name} - ₹{item.price}</span>
            <button onClick={() => addToCart(item)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GroceryList;
