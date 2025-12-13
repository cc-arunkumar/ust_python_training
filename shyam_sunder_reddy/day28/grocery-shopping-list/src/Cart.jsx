function Cart({ cartItems, removeFromCart, updateQuantity }) {
  const totalPrice = cartItems.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  const discountApplied = totalPrice > 1000;
  const finalPrice = discountApplied ? totalPrice * 0.9 : totalPrice;

  return (
    <div style={{ flex: 1 }}>
      <h2>🛒 Your Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              <strong>{item.name}</strong> - ₹{item.price} × {item.quantity} = ₹
              {item.price * item.quantity}
              <div>
                <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>
                <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
                <button className="remove" onClick={() => removeFromCart(item.id)}>Remove</button>
              </div>
            </li>
          ))}
        </ul>
      )}

      <div className="cart-summary">
        <h3>Total: ₹{totalPrice}</h3>
        {discountApplied && (
          <p>🎉 Discount Applied! 10% off → Final Price: <strong>₹{finalPrice}</strong></p>
        )}
      </div>
    </div>
  );
}

export default Cart;
