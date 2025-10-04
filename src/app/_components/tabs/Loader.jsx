import React from "react";

const Loader = () => {
  return (
    <div className="w-full h-96 flex items-center justify-center">
      <div className="w-16 aspect-square border-4 rounded-full border-primary border-t-transparent animate-spin" />
    </div>
  );
};

export default Loader;
