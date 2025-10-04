"use client";
import React, { useState } from "react";

import History from "./tabs/History";
import Threats from "./tabs/Threats";
import Status from "./tabs/Status";

const LiveData = () => {
  const [activeTab, setActiveTab] = useState("status");

  const tabs = [
    { id: "status", label: "Status" },
    { id: "history", label: "Nasa Data" },
    { id: "threats", label: "Threats" },
  ];

  const renderTabContent = () => {
    switch (activeTab) {
      case "status":
        return <Status />;

      case "threats":
        return <Threats />;
      case "history":
        return <History />;
      default:
        return null;
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto mt-10">
      <h2 className="text-3xl font-bold  tracking-tight mb-8 text-center">
        Keep updated with live data about Abu Simbel
      </h2>
      <div className="border-b border-gray-200">
        <nav className="-mb-px flex space-x-8">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`py-2 px-1 border-b-2 font-medium text-sm transition-colors duration-200 ${
                activeTab === tab.id
                  ? "border-blue-500 text-blue-600"
                  : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      <div className="mt-6">{renderTabContent()}</div>
    </div>
  );
};

export default LiveData;
