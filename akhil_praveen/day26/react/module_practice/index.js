import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
// import { toUpperCase,toLowerCase } from "./utils/string.js";
// import { add,sub,multiply,division } from "./utils/math.js";
// import {theme, toggleTheme } from "./config/theme.js";

import {toUpperCase,toLowerCase, add,sub,multiply,division ,theme, toggleTheme } from "./indexUtils.js";

Header(10);
Footer(10);

console.log(toLowerCase("GADGA"));
console.log(toUpperCase("hdhg"));

console.log(add(11,20))
console.log(sub(11,20))
console.log(multiply(11,20))
console.log(division(11,20))

console.log(theme)
toggleTheme()
console.log(theme)