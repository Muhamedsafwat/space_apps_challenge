import React, { useState, useEffect } from "react";
import Loader from "./Loader";

const History = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getData = async () => {
      const res = await fetch(`${process.env.NEXT_PUBLIC_CHAT_API}/nasa-data`);
      const data = await res.json();
      setData(data);
      setLoading(false);
    };
    getData();
  }, []);
  return (
    <div className="p-6">
      <h3 className="text-xl font-semibold mb-4">Nasa Data</h3>
      {loading ? (
        <Loader />
      ) : data?.events?.length == 0 ? (
        <p>There are no data available</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Total Subsidence Card */}
          <div className="bg-gradient-to-br from-red-50 to-red-100 border border-red-200 rounded-lg p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-red-500 rounded-lg">
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"
                  />
                </svg>
              </div>
              <span className="text-red-600 text-sm font-medium">
                Subsidence
              </span>
            </div>
            <h4 className="text-2xl font-bold text-gray-900 mb-1">
              {data?.total_subsidence_mm || "-12.8"} mm
            </h4>
            <p className="text-gray-600 text-sm">
              Total subsidence over period
            </p>
          </div>

          {/* Annual Rate Card */}
          <div className="bg-gradient-to-br from-orange-50 to-orange-100 border border-orange-200 rounded-lg p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-orange-500 rounded-lg">
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <span className="text-orange-600 text-sm font-medium">Rate</span>
            </div>
            <h4 className="text-2xl font-bold text-gray-900 mb-1">
              {data?.annual_rate_mm_per_year || "-3.2"} mm/year
            </h4>
            <p className="text-gray-600 text-sm">Annual subsidence rate</p>
          </div>

          {/* Observation Period Card */}
          <div className="bg-gradient-to-br from-blue-50 to-blue-100 border border-blue-200 rounded-lg p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-blue-500 rounded-lg">
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                  />
                </svg>
              </div>
              <span className="text-blue-600 text-sm font-medium">Period</span>
            </div>
            <h4 className="text-2xl font-bold text-gray-900 mb-1">
              {data?.observation_period_years || "4.0"} years
            </h4>
            <p className="text-gray-600 text-sm">Observation period</p>
          </div>

          {/* Peak Movement Card */}
          <div className="bg-gradient-to-br from-purple-50 to-purple-100 border border-purple-200 rounded-lg p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-purple-500 rounded-lg">
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                  />
                </svg>
              </div>
              <span className="text-purple-600 text-sm font-medium">Peak</span>
            </div>
            <h4 className="text-2xl font-bold text-gray-900 mb-1">
              {data?.peak_movement_mm || "-15.2"} mm
            </h4>
            <p className="text-gray-600 text-sm">Peak movement recorded</p>
          </div>

          {/* Water Level Correlation Card */}
          <div className="bg-gradient-to-br from-green-50 to-green-100 border border-green-200 rounded-lg p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-green-500 rounded-lg">
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                  />
                </svg>
              </div>
              <span className="text-green-600 text-sm font-medium">
                Correlation
              </span>
            </div>
            <h4 className="text-2xl font-bold text-gray-900 mb-1">
              {data?.water_level_correlation || "0.73"}
            </h4>
            <p className="text-gray-600 text-sm">Water level correlation</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default History;
