const groceryItems = [
  { id: 1, name: "Rice", price: 50 },
  { id: 2, name: "Wheat", price: 40 },
  { id: 3, name: "Tomatoes", price: 30 },
  { id: 4, name: "Milk", price: 20 },
  { id: 5, name: "Potatoes", price: 25 },
];

export default function GroceryList({ onAddToCart }) {
  return (
    <div className="grocery-section">
      <h2 className="section-title">Available Groceries</h2>
      <div className="grocery-grid">
        {groceryItems.map((item) => (
          <div key={item.id} className="grocery-card">
            <h3 className="item-name">{item.name}</h3>
            <p className="item-price">₹{item.price}</p>
            <button onClick={() => onAddToCart(item)} className="add-btn">
              Add to Cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
