// import { defineConfig } from 'vite';
// // If you're using React, Vue, etc., keep your existing plugin (e.g., import react from '@vitejs/plugin-react')
// // import react from '@vitejs/plugin-react'; // example

// import tailwindcss from '@tailwindcss/vite';

// export default defineConfig({
//   plugins: [
//     // react(), // your framework plugin if any
//     tailwindcss(),
//   ],
// });



import { defineConfig } from 'vite';
// import your framework plugin if needed, e.g.:
// import react from '@vitejs/plugin-react';

import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    // react(),  // your other plugins first
    tailwindcss(),
  ],
});