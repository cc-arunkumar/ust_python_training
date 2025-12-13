import React from "react";
 
function GroceryList({ items, addToCart }) {
  return (
    <div>
      <h2 >Grocery List</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id} style={{ marginBottom: "10px" }}>
            {item.name} - ₹{item.price}{" "}
            <button className="add_button" onClick={() => addToCart(item)}>
              Add to Cart
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
 
export default GroceryList;
 
 onabort