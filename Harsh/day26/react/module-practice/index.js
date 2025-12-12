import Header from './components/Header.js'
import Footer from './components/Footer.js'
import { toLowerCase,toUpperCase } from './export.js'
import { add,sub,mul,div } from './export.js'
import { theme,toggle } from './export.js'

Header(10)
Footer()

console.log(toUpperCase("hello"),toLowerCase("HELLO"))
console.log(add(1,2),sub(1,2),mul(1,2),div(1,2))
console.log(toggle(),theme)