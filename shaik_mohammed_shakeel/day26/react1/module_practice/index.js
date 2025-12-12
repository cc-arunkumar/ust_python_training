import Header from './components/Header.js';  
import Footer from './components/Footer.js';  
import  {toUpperCase,toLowerCase}  from './utils/string.js';
import { toggleTheme } from './config/theme.js';
import { addition,subtract,multiply,divide } from './utils/maths.js';

Header("Welcome to the React App!");  
Footer();

console.log(toUpperCase("hello world"));
console.log(toLowerCase("HELLO WORLD"));
console.log(addition(10,5))
console.log(subtract(10,5))
console.log(multiply(10,5))
console.log(divide(10,5))
console.log(toggleTheme(light))