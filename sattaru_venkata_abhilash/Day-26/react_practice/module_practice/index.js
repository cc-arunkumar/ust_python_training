// Import everything from indexUtils.js
import { 
    theme, 
    toggleTheme, 
    Header, 
    Footer, 
    add, 
    subtract, 
    multiply, 
    divide, 
    capitalize, 
    reverse 
} from './indexUtils.js';  

console.log(theme); 

toggleTheme();
console.log(theme);  

Header("Welcome to the site!");
Footer();

console.log(add(5, 3));       
console.log(subtract(10, 5));  
console.log(multiply(4, 6));   

try {
    console.log(divide(10, 0));
} catch (error) {
    console.error(error.message);  
}

console.log(capitalize("hello"));  // Output: Hello
console.log(reverse("world"));    // Output: dlrow
