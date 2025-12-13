import React from "react";

function GroceryList({ groceryItems, addToCart }) {
  return (
    <div>
      <h2>Available Groceries</h2>
      <ul>
        {groceryItems.map((item) => (
          <li key={item.id}>
            {item.name} - ₹{item.price}{" "}
            <button onClick={() => addToCart(item)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GroceryList;
