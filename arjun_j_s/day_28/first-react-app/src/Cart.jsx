import React from "react";

function Cart({ cartItems, removeFromCart, updateQuantity }) {
  const total = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  const discount = total > 1000 ? total * 0.1 : 0;
  const finalPrice = total - discount;

  return (
  <div className="card">
    <h2>Cart</h2>

    {cartItems.length === 0 && (
      <p className="empty-cart">Your cart is empty</p>
    )}


      {cartItems.map((item) => (
        <div key={item.id} style={{ marginBottom: "10px" }}>
          <strong>{item.name}</strong> - ₹{item.price} ×
          <input
            type="number"
            value={item.quantity}
            min="1"
            onChange={(e) =>
              updateQuantity(item.id, Number(e.target.value))
            }
            style={{ width: "50px", margin: "0 10px" }}
          />
          = ₹{item.price * item.quantity}
          <button
            className="remove-btn"
            onClick={() => removeFromCart(item.id)}
          >
            Remove
          </button>
        </div>
      ))}

      <hr />

      <div className="cart-summary">
        <p>Total: ₹{total}</p>

        {discount > 0 && (
          <p className="discount">
            Discount Applied (10%): -₹{discount}
          </p>
        )}

        <h3 className="final-price">
          Final Price: ₹{finalPrice}
        </h3>
      </div>
    </div>
  );
}

export default Cart;
