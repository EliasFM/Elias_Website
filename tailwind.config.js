/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './website/templates/**/8.html',
    './pages/templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"),require('daisyui')],
  daisyui: {
    themes: ["light", "dark", "cupcake"], // add the themes you want here
  },
};