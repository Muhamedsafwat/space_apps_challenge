import React from "react";

const Hero = () => {
  return (
    <section
      className="relative h-screen bg-cover bg-center"
      style={{
        backgroundImage: `url('https://lh3.googleusercontent.com/aida-public/AB6AXuDA_okX0819QYA72MfJjUDjiF3z-S049dv6o7EXezTB_XKsw73DthF0bhuLuyIK07Pk-oLOLG8pBIRJ8WnxQLvhOnNMUI6I4C9_dQuNufI5xLPNJQjydel_sI3ZmjrlkgEKRLiIEdonfAqrmMEjZ2gM921qJLAofUL1kcM4VYDGSYSzx_GA7UPo7BWQmjyKSPgRlqroT0mxGYGdMWXEy8S5jYT-NlvM2eSdfwR-U99F4aJPDyNbrgQl2bpgMZd8AeVjj3Fjh9zW2e0')`,
      }}
    >
      <div className="absolute inset-0 bg-black/50"></div>
      <div className="relative z-10 flex flex-col items-center justify-center h-full text-center text-white px-4">
        <h1 className="text-5xl md:text-7xl font-bold tracking-tighter mb-4">
          Guardians of a Timeless Legacy
        </h1>
        <p className="text-lg md:text-2xl max-w-3xl leading-relaxed mb-8">
          Protecting Egypt's monumental heritage from the escalating threats of
          environmental change.
        </p>
        <button className="flex min-w-[84px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-6 bg-primary text-white text-base font-bold shadow-lg shadow-primary/30 hover:bg-primary/90 transition-all">
          <span className="truncate">Discover Our Mission</span>
        </button>
      </div>
    </section>
  );
};

export default Hero;
