"use client";
import React from "react";
import ReactCompareImage from "react-compare-image";

const Sample = () => {
  return (
    <section>
      <h2 className="text-3xl font-bold  tracking-tight text-center mb-8">
        NISAR in Action: A Clearer Picture
      </h2>
      <p className=" leading-relaxed max-w-3xl mx-auto mb-8 text-center">
        The difference is stark. While standard optical satellite images show us
        the surface, NISAR's radar penetrates further, revealing underlying
        vulnerabilities. Below, compare a standard view with a NISAR-processed
        image that highlights subtle ground shifts near a critical heritage
        site.
      </p>
      <div className="w-full aspect-video overflow-hidden relative">
        <div className="top-1/2 -translate-y-1/2 absolute w-full aspect-video">
          <ReactCompareImage
            leftImage="https://lh3.googleusercontent.com/aida-public/AB6AXuBvV0IrWm4UWZgXX8VOxO8mshK1XeYs6XeNQi1JrA0t64d80oq9chJDU18__XdYLg13G-rrAODYV_LmBpbn3cwtaqo0QD4VhIbejmYk6-tfvpDTXJfkhAsMjFjCEGDsOYhUYcqngSoSjAvnsD_UL2pXvXdYHDV0JOp-5S8E3J4Uu75230Pu8RmWuOwFUtZo_9IN68KX1-r1E1vEwLyeuKoYTz02td7ANBJGEuxFRBqZw08Iubso30pfD8mnwN0Nnk8sFEjWhWUNqq4"
            rightImage="https://lh3.googleusercontent.com/aida-public/AB6AXuA2j1nk3i7UaSaeB4keeuUVljyfxsCcIFswnl_1psg8lZYghU0XSbkTw7-5UPwNXLklpWwqb5fOuCDkw7S_fa4SPGDO2IL1vBDKYUpzZ0tN9Z8Xv-KlfD3Fp-j2mUvjYedqdo7uV4p9US-ZGD37VFneE1oObQGYtj446CLABijYG0U10hBacyYv-rKou0whyFYzOP2CSCfAzOxKXpGc4Br14zXKWctGNWaFiOjRwPGNcSr-LQ4nJfglmc3qyZbiyEJgShyCDBnJHug"
          />
        </div>
      </div>
      <p className="text-center mt-4 leading-relaxed">
        The vibrant colors in the NISAR image are not artistic flair; they
        represent data-driven insights into ground movement, allowing us to
        pinpoint areas requiring immediate attention and plan targeted
        preservation strategies before irreversible damage occurs.
      </p>
    </section>
  );
};

export default Sample;
