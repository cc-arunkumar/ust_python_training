function GroceryList({ items, addToCart }) {
  return (
    <div style={{ flex: 1 }}>
      <h2>🛍️ Available Groceries</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <strong>{item.name}</strong> - ₹{item.price}
            <button onClick={() => addToCart(item)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GroceryList;
