import Header from './components/Header.js'
import Footer from './components/Footer.js'
import {toLowerCase,toUpperCase} from './utils/string.js'
import {add,subtract,multiply,divide} from './utils/math.js'
import {toggleTheme} from './indexutils.js'


Header(10)
Footer()
console.log(toUpperCase("hello world"))
console.log(toLowerCase("HELLO WORLD"))
console.log(add(6,3))
console.log(subtract(6,3))
console.log(multiply(6,3))
console.log(divide(6,3))
console.log(toggleTheme())