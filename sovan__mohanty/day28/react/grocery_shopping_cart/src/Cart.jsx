function Cart({ cartItems, removeFromCart, updateQuantity }) {
  const total = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  const discountApplied = total > 1000;
  const finalTotal = discountApplied ? total * 0.9 : total;

  return (
    <div>
      <h2>Your Cart</h2>
      {cartItems.length === 0 ? (
        <p>No items in cart.</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - ₹{item.price} ×
              <input
                type="number"
                min="1"
                value={item.quantity}
                onChange={(e) => updateQuantity(item.id, e.target.value)}
              />
              = ₹{item.price * item.quantity}
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
      )}

      <h3>Total: ₹{total}</h3>
      {discountApplied && (
        <p className="discount">
        Discount Applied! 10% off → Final Total: ₹{finalTotal}
        </p>
      )}
    </div>
  );
}

export default Cart;
