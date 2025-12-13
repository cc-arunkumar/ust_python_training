import React from "react";

const GroceryList = ({ items, onAddToCart }) => {
  return (
    <div className="grocery-list">
      <h3 className="section-title">Available Groceries</h3>
      <div className="item-list">
        {items.map((item) => (
          <div className="item" key={item.id}>
            <div style={{display:'flex',gap:12,alignItems:'center'}}>
              <div style={{width:52,height:52,borderRadius:10,background:'#eef2ff',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700,color:'#4466ff'}}>
                {item.name.charAt(0).toUpperCase()}
              </div>
              <div>
                <div className="item-name">{item.name}</div>
                <div className="item-meta">Price: <span className="price">₹{Number(item.price).toFixed(2)}</span></div>
              </div>
            </div>
            <div style={{display:'flex',justifyContent:'flex-end',marginTop:10}}>
              <button className="add-btn" onClick={() => onAddToCart(item)} aria-label={`Add ${item.name} to cart`}>
                + Add
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GroceryList;
 