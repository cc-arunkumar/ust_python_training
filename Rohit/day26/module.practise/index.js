import Rohit from "./components/Header.js";
import Footer from "./components/Footer.js";

import multiply from './utils/math.js';

// import { add, subtract, divide }  from './utils/math.js';
// import  {toggleTheme} from "./config/theme.js"

// import { toUpperCase,toLowerCase } from "./utils/strimg.js";

import {add,subtract,divide,toLowerCase,toUpperCase,toggleTheme} from "./indexUtils.js"
Rohit()
Footer(10)

console.log(add(2, 3));       
console.log(subtract(5, 2));  
console.log(multiply(4, 6))
console.log(divide(12, 6))
console.log(toggleTheme("dark"))