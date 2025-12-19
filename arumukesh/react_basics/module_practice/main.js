// import header from './components/header.js';
// import footer from './components/footer.js';
import {header,footer} from './index_utils.js';
header();
footer();

import { toggletheme ,theme} from './config/theme.js';
console.log("current theme:",theme);
toggletheme();
console.log("after toggle theme:",theme);
