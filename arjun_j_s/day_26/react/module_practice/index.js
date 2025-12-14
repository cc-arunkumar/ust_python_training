import Header from "./components/Header.js";
import Footer from "./components/Footer.js";

import {theme,toogleTheme,toLowerCase,toUpperCase,add,subtract,multiply,divide} from "./indexUtils.js";

Header(10);
Footer();

console.log(toLowerCase("ARJUNNNNNN"))
console.log(toUpperCase("arjuuuuuuu"))

console.log("Add:",add(1,2))
console.log("Subtract:",subtract(2,1))
console.log("Multiply:",multiply(5,10))
console.log("Divide:",divide(7,7))

console.log(theme)
toogleTheme()
console.log(theme)