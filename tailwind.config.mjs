/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./src/**/*.{html,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#1193d4",
        background: "#101c22",
      },
      fontFamily: {
        display: ["Space Grotesk"],
      },
    },
  },
  plugins: [],
};
