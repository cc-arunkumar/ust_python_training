export default function Cart({
  cartItems,
  onRemoveItem,
  onUpdateQuantity,
  totalPrice,
  discount,
}) {
  if (cartItems.length === 0) {
    return (
      <div className="cart-section">
        <h2 className="section-title">Shopping Cart</h2>
        <p className="empty-cart">Your cart is empty</p>
      </div>
    );
  }

  const subtotal = totalPrice;
  const discountAmount = discount ? subtotal * 0.1 : 0;
  const finalTotal = subtotal - discountAmount;

  return (
    <div className="cart-section">
      <h2 className="section-title">Shopping Cart</h2>
      <div className="cart-items">
        {cartItems.map((item) => (
          <div key={item.id} className="cart-item">
            <div className="item-details">
              <h3 className="cart-item-name">{item.name}</h3>
              <p className="cart-item-price">
                ₹{item.price} × {item.quantity}
              </p>
            </div>
            <div className="item-controls">
              <div className="quantity-controls">
                <button
                  onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
                  className="qty-btn"
                >
                  -
                </button>
                <span className="quantity">{item.quantity}</span>
                <button
                  onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
                  className="qty-btn"
                >
                  +
                </button>
              </div>
              <button
                onClick={() => onRemoveItem(item.id)}
                className="remove-btn"
              >
                Remove
              </button>
            </div>
            <p className="item-total">₹{item.price * item.quantity}</p>
          </div>
        ))}
      </div>

      <div className="cart-summary">
        <div className="summary-row">
          <span>Subtotal:</span>
          <span>₹{subtotal}</span>
        </div>
        {discount && (
          <div className="summary-row discount-row">
            <span>Discount (10%):</span>
            <span>-₹{discountAmount.toFixed(2)}</span>
          </div>
        )}
        <div className="summary-row total-row">
          <span>Total:</span>
          <span>₹{finalTotal.toFixed(2)}</span>
        </div>
        {discount && (
          <p className="discount-message">
            🎉 You saved ₹{discountAmount.toFixed(2)}!
          </p>
        )}
      </div>
    </div>
  );
}
