/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./src/**/*.{html,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#d8a429",
        background: "#f5f5f5",
      },
      fontFamily: {
        display: ["Space Grotesk"],
      },
    },
  },
  plugins: [],
};
