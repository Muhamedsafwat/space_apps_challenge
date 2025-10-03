import React from "react";

const Navbar = () => {
  return (
    <header className="flex items-center justify-between whitespace-nowrap border-b border-white/10 px-10 py-4 fixed w-full backdrop-blur-sm z-50 bg-primary/80">
      <div className="flex items-center gap-4 text-white">
        <svg
          className="h-6 w-6 text-primary"
          fill="none"
          viewBox="0 0 48 48"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M6 6H42L36 24L42 42H6L12 24L6 6Z" fill="currentColor"></path>
        </svg>
        <h2 className="text-xl font-bold tracking-tight">Preserve Egypt</h2>
      </div>
      <div className="flex flex-1 justify-end gap-6 items-center">
        <nav className="hidden md:flex items-center gap-6">
          <a
            className="text-sm font-medium text-slate-300 :hover:text-primary transition-colors"
            href="#"
          >
            Home
          </a>
          <a
            className="text-sm font-medium text-slate-300 hover:text-primary dark:hover:text-primary transition-colors"
            href="#"
          >
            About
          </a>
          <a
            className="text-sm font-medium text-slate-300 hover:text-primary dark:hover:text-primary transition-colors"
            href="#"
          >
            Projects
          </a>
          <a
            className="text-sm font-medium text-slate-300 hover:text-primary dark:hover:text-primary transition-colors"
            href="#"
          >
            Contact
          </a>
        </nav>
        <button className="flex min-w-[84px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 px-5 bg-primary text-white text-sm font-bold shadow-lg shadow-primary/30 hover:bg-primary/90 transition-all">
          <span className="truncate">Donate</span>
        </button>
      </div>
    </header>
  );
};

export default Navbar;
