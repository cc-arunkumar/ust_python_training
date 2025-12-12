import { toUpperCase, multiply, divide, add, theme, toggleTheme } from "./indexUtils.js";
// Header("Arguement");
// Footer();
console.log(toUpperCase("hello world!"))


console.log(multiply(5, 10));
console.log(divide(50, 10));
console.log(add(5, 10));
console.log(`Current theme: ${theme}`);
toggleTheme();
console.log(`Theme after toggle: ${theme}`);