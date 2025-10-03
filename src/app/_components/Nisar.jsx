import React from "react";

const Nisar = () => {
  return (
    <section className="text-center">
      <h2 className="text-3xl font-bold  tracking-tight mb-4">
        Our Eye in the Sky: The NISAR Satellite
      </h2>
      <p className=" leading-relaxed max-w-3xl mx-auto mb-12">
        The NASA-ISRO Synthetic Aperture Radar (NISAR) satellite is a
        game-changer. This advanced mission provides an unprecedented,
        all-weather, day-and-night view of Earth, allowing us to detect subtle,
        yet critical, changes to our planet's surface and our heritage sites.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 ">
        <div className="flex flex-col items-center gap-4">
          <div className="bg-primary/10 p-4 rounded-full">
            <svg
              className="h-12 w-12 text-primary"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M5 12s2.5-8 7-8 7 8 7 8-2.5 8-7 8-7-8-7-8z"></path>
              <circle cx="12" cy="12" r="3"></circle>
            </svg>
          </div>
          <h3 className="font-bold text-xl">Radar Vision</h3>
          <p>
            Sees through clouds and darkness, providing constant monitoring.
          </p>
        </div>
        <div className="flex flex-col items-center gap-4">
          <div className="bg-primary/10 p-4 rounded-full">
            <svg
              className="h-12 w-12 text-primary"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
              <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
              <line v-if="false" x1="12" x2="12" y1="22.08" y2="12"></line>
            </svg>
          </div>
          <h3 className="font-bold text-xl">Precision Data</h3>
          <p>Measures ground deformation with centimeter-level accuracy.</p>
        </div>
        <div className="flex flex-col items-center gap-4">
          <div className="bg-primary/10 p-4 rounded-full">
            <svg
              className="h-12 w-12 text-primary"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <h3 className="font-bold text-xl">Global Coverage</h3>
          <p>
            Systematically maps Earth every 12 days for rapid change detection.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Nisar;
