import React from "react";

const Gallery = () => {
  return (
    <section>
      <h2 className="text-3xl font-bold text-slate-800 dark:text-white tracking-tight text-center mb-8">
        Gallery of Impact
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="relative group overflow-hidden rounded-xl">
          <img
            alt="Erosion on a temple wall"
            className="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuA2j1nk3i7UaSaeB4keeuUVljyfxsCcIFswnl_1psg8lZYghU0XSbkTw7-5UPwNXLklpWwqb5fOuCDkw7S_fa4SPGDO2IL1vBDKYUpzZ0tN9Z8Xv-KlfD3Fp-j2mUvjYedqdo7uV4p9US-ZGD37VFneE1oObQGYtj446CLABijYG0U10hBacyYv-rKou0whyFYzOP2CSCfAzOxKXpGc4Br14zXKWctGNWaFiOjRwPGNcSr-LQ4nJfglmc3qyZbiyEJgShyCDBnJHug"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
          <div className="absolute bottom-0 left-0 p-4">
            <h3 className="text-white font-bold text-lg">
              Salt Crystallization Damage
            </h3>
            <p className="text-slate-200 text-sm">
              Porous stone is crumbling due to salt carried by rising damp.
            </p>
          </div>
        </div>
        <div className="relative group overflow-hidden rounded-xl">
          <img
            alt="Flooding near a monument"
            className="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuC-_T8Y1vLoUodBVHuZlqCZW24vjnbcuQDW6Z0OGYneAPSp_Nn2nvrjif9F3hiIL3IiuG40T0DmflTbgN_VPhme3NmqloTAc04vTH6ma1sR5kjT_QOFHJc63u4rGG67X99s98IMlitcfThLD1GSB_WI7hWSqbH-YlXmMYXo3nlWvOyqu2bTCIUst_fyVnFrXMwBImJ8fMO7w7-h0xeNn_fGSP0P-FsBNNCPwi7ykemPjCDIgj9slRgEnJkTHn4rQkPeUAyGeLSxFzY"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
          <div className="absolute bottom-0 left-0 p-4">
            <h3 className="text-white font-bold text-lg">Flooding Risks</h3>
            <p className="text-slate-200 text-sm">
              Increased flooding threatens the foundations of riverside temples.
            </p>
          </div>
        </div>
        <div className="relative group overflow-hidden rounded-xl">
          <img
            alt="Cracks in a stone structure"
            className="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuCnn9vAbsL9la2fzx8JeH30LQykhV0fOenDT-2rMRSinze-jy84f0fBsT6rh-zJUT54pj30yZIqNai2zOyqlhyKao723bacQ8Hz9fsoz9nodpZ120vrn5wiTlexSRTpgTpuHzeQaTJ5KVkpZdO-TxQAdcinLCK-W6_jPVBNdBHR81Mm1kRP28_btqf70yiZ0JQEPK48SGOfFqdSogjv3d0ygXif3Yo5LFxS_WoPdO3wJmYOXEy8Q5UPoDFZ56XWDqaQfN169KYq5k0"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
          <div className="absolute bottom-0 left-0 p-4">
            <h3 className="text-white font-bold text-lg">
              Structural Instability
            </h3>
            <p className="text-slate-200 text-sm">
              Extreme heat and ground shifts cause dangerous fractures.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Gallery;
