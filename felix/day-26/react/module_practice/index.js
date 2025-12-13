import header from "./components/header.js";
import footer from "./components/footer.js";

import {to_uppercase,to_lowercase,addition,subtraction,multiplication,division,theme,toggletheme} from "./index_utils.js";


header(10);
footer(20);

console.log(to_uppercase("hello world"))
console.log(to_lowercase("HELLO WORLD"))

console.log(addition(1,2))
console.log(subtraction(1,2))
console.log(multiplication(1,2))
console.log(division(1,2))
console.log(theme)
toggletheme()
console.log(theme)