import React from "react";

const Chatbot = () => {
  return (
    <div className="fixed bottom-5 right-5 z-50">
      <button className="bg-primary hover:bg-primary/90 text-white rounded-full p-4 shadow-xl flex items-center justify-center gap-3 transition-all group w-16 h-16 hover:w-48">
        <svg
          className="h-8 w-8"
          fill="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM9.5 11.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zm4.5 0c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5z"></path>
        </svg>
        <span className="font-bold whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          AI Chatbot
        </span>
      </button>
    </div>
  );
};

export default Chatbot;
