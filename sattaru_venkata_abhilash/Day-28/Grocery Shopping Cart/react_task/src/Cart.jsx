import React from 'react';

const Cart = ({ cartItems, onRemoveFromCart, onChangeQuantity, totalPrice, discountApplied, dynamicDiscountStyle, onClearCart, onCheckout, totalItems }) => {
  const fmt = (v) => Number(v).toFixed(2);

  return (
    <div className="cart">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h2 className="section-title">Your Cart</h2>
        {cartItems.length > 0 && (
          <button className="btn ghost" onClick={onClearCart} aria-label="Clear cart">Clear</button>
        )}
      </div>

      {cartItems.length === 0 ? (
        <p style={{color:'#6b7280'}}>Your cart is empty — add some groceries to get started.</p>
      ) : (
        <div className="cart-items">
          {cartItems.map(item => (
            <div key={item.id} className="cart-item">
              <div className="left">
                <div className="name">{item.name}</div>
                <div className="meta">₹{fmt(item.price)} each</div>
              </div>

              <div style={{display:'flex',flexDirection:'column',alignItems:'flex-end',gap:8}}>
                <div className="qty-control">
                  <button aria-label={`Decrease ${item.name} quantity`} onClick={() => onChangeQuantity(item.id, Math.max(1, item.quantity - 1))}>-</button>
                  <div className="num">{item.quantity}</div>
                  <button aria-label={`Increase ${item.name} quantity`} onClick={() => onChangeQuantity(item.id, item.quantity + 1)}>+</button>
                </div>

                <div className="meta">Total: <strong>₹{fmt(item.price * item.quantity)}</strong></div>
                <div style={{display:'flex',gap:8,marginTop:6}}>
                  <button className="remove-link" onClick={() => onRemoveFromCart(item.id)}>Remove</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      <div className="cart-summary">
        <p className="total">Subtotal: ₹{fmt(totalPrice)}</p>
        {discountApplied && (
          <p className="discount" style={dynamicDiscountStyle}>Discount Applied: 10% Off</p>
        )}
        <p className="final">Final Price: ₹{fmt(discountApplied ? totalPrice * 0.9 : totalPrice)}</p>
        <div style={{display:'flex',justifyContent:'flex-end',gap:10,marginTop:10}}>
          <button className="btn ghost" onClick={onClearCart} disabled={cartItems.length===0}>Clear</button>
          <button className="btn" onClick={onCheckout} disabled={cartItems.length===0}>Checkout</button>
        </div>
        <div style={{marginTop:8,color:'#6b7280',fontSize:'.95rem'}}>Items in cart: <strong>{totalItems}</strong></div>
      </div>
    </div>
  );
};

export default Cart;
 