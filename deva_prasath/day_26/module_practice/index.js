import Header from '/indexUtils.js';
import footer from './components/Footer.js';
import {toUpperCase ,toLowerCase} from './utils/string.js';

import {add,subtract,multiply,divide} from './utils/math.js'
import { toggleTheme } from './config/theme.js';

Header(toUpperCase("Deva"))
footer(toLowerCase("Prasath"))

console.log(add(5,10))
console.log(subtract(5,10))
console.log(multiply(5,10))
console.log(divide(5,10))
console.log(toggleTheme())

