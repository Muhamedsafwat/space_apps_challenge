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
            leftImage="/images/earth1.png"
            rightImage="/images/nisar1.png"
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
