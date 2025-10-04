import React, { useState, useEffect } from "react";
import Loader from "./Loader";

const Threats = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getData = async () => {
      const res = await fetch(`${process.env.NEXT_PUBLIC_CHAT_API}/threats`);
      const data = await res.json();
      setData(data);
      setLoading(false);
    };
    getData();
  }, []);
  return (
    <div className="p-6">
      <h3 className="text-xl font-semibold mb-4">Threats</h3>
      {loading ? (
        <Loader />
      ) : data?.threats?.length == 0 ? (
        <p>There are no Threats detected</p>
      ) : (
        <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
          <table className="w-full text-sm text-left rtl:text-right text-gray-500 ">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50  ">
              <tr>
                <th scope="col" className="px-6 py-3">
                  Threat
                </th>
                <th scope="col" className="px-6 py-3">
                  Severety
                </th>
                <th scope="col" className="px-6 py-3">
                  Impact
                </th>
                <th scope="col" className="px-6 py-3">
                  Status
                </th>
              </tr>
            </thead>
            <tbody>
              {data.threats.map((item, index) => (
                <tr
                  key={index}
                  className="bg-white border-b -gray-700 border-gray-200 hover:bg-gray-50 "
                >
                  <th
                    scope="row"
                    className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap "
                  >
                    {item.name}
                  </th>
                  <td className="px-6 py-4">
                    <span
                      className={`px-3 py-1 rounded-full block text-center ${
                        item.severity == "low"
                          ? "bg-green-400"
                          : "bg-yellow-400"
                      }`}
                    >
                      {item.severity}
                    </span>
                  </td>
                  <td className="px-6 py-4">{item.impact}</td>
                  <td className="px-6 py-4">{item.current_status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Threats;
