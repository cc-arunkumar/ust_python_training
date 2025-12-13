import React from "react";

// GroceryList component receives a list of items and a function to handle adding items to the cart
const GroceryList = ({ items, onAddToCart }) => {
  return (
    <div className="grocery-list">
      <h2>Available Groceries</h2>
      <div className="item-list">
        {/* Iterate over the items array and render each item */}
        {items.map((item) => (
          <div className="item" key={item.id}>
            {/* Display item name and price */}
            <p>
              {item.name} - ₹{item.price}
            </p>
            {/* Button to add item to the cart */}
            <button onClick={() => onAddToCart(item)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GroceryList;
