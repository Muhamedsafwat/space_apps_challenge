import React from "react";

const CTA = () => {
  return (
    <div className="flex justify-center mt-8">
      <button className="flex min-w-[84px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-6 bg-primary text-white text-base font-bold shadow-lg shadow-primary/30 hover:bg-primary/90 transition-all">
        <span className="truncate">Join the Preservation Effort</span>
      </button>
    </div>
  );
};

export default CTA;
