import footer from "./components/footer.js";
import header from "./components/header.js";
// import { ToLowerCase,ToUpperCase } from "./utils/string.js";
// import {add,subtract,divide,multiply} from "./utils/math.js";
// import { toggleTheme,theme } from "./config/theme.js";
import {ToLowerCase,ToUpperCase,add,subtract,divide,multiply,toggleTheme,theme} from "./indexUtils.js";

header("welcome");
footer();
console.log(ToLowerCase("ARUN"));
console.log(ToUpperCase("arun"));
console.log(add(2,3));
console.log(subtract(3,2));
console.log(multiply(2,3));
console.log(divide(5,2));
console.log(theme)
toggleTheme()
console.log(theme)

