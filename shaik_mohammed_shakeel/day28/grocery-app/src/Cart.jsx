import React from 'react';
 
const Cart = ({ cartItems, onRemoveFromCart, onChangeQuantity, totalPrice, discountApplied, dynamicDiscountStyle }) => {
  return (
    <div className="cart">
      <h2>Your Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <div className="cart-items">
          {cartItems.map(item => (
            <div key={item.id} className="cart-item">
              <p>{item.name} - ₹{item.price}</p>
              <input
                type="number"
                min="1"
                value={item.quantity}
                onChange={(e) => onChangeQuantity(item.id, parseInt(e.target.value))}
              />
              <p>Total: ₹{item.price * item.quantity}</p>
              <button onClick={() => onRemoveFromCart(item.id)}>Remove</button>
            </div>
          ))}
        </div>
      )}
      <div className="cart-total">
        <p>Total Price: ₹{totalPrice}</p>
        {discountApplied && (
          <p className="discount" style={dynamicDiscountStyle}>Discount Applied: 10% Off</p>
        )}
        <p>Final Price: ₹{discountApplied ? totalPrice * 0.9 : totalPrice}</p>
      </div>
    </div>
  );
};
 
export default Cart;