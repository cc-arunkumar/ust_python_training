import React from "react";

const ProductCard = ({name , price,rating})=>{
    return(
        <div className="card1">
            <h4>{name}</h4>
            <p>Rating:{rating}</p>
            <p>cost:{price}</p>
        </div>
    );
};
 export default ProductCard;