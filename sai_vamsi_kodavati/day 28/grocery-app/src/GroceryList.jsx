import React from "react";
 
const GroceryList = ({ items, onAddToCart }) => {
  return (
    <div className="grocery-list">
      <h2>Available Groceries</h2>
      <div className="item-list">
        {items.map((item) => (
          <div className="item" key={item.id}>
            <p>
              {item.name} - ₹{item.price}
            </p>
            <button onClick={() => onAddToCart(item)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
};
 
export default GroceryList