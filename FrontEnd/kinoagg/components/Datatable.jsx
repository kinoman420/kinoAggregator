import React, { useEffect, useState } from 'react';

const DataTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Replace with your API endpoint
    fetch('/api/data')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white">
        <thead className="bg-gray-800 text-white">
          <tr>
            <th className="w-1/6 py-2 px-4">Category</th>
            <th className="w-1/2 py-2 px-4">Name</th>
            <th className="w-1/12 py-2 px-4">Link</th>
            <th className="w-1/12 py-2 px-4">Size</th>
            <th className="w-1/6 py-2 px-4">Date</th>
            <th className="w-1/12 py-2 px-4">↑</th>
            <th className="w-1/12 py-2 px-4">↓</th>
            <th className="w-1/12 py-2 px-4">✓</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index} className="text-center border-b">
              <td className="py-2 px-4">
                <img src={item.category_image} alt={item.category} className="w-16 h-8 object-contain"/>
              </td>
              <td className="py-2 px-4 text-left">
                <a href={item.link} className="text-blue-600 hover:underline">{item.title}</a>
              </td>
              <td className="py-2 px-4">
                <a href={item.magnet} className="text-blue-600 hover:underline">🔗</a>
              </td>
              <td className="py-2 px-4">{item.size}</td>
              <td className="py-2 px-4">{item.date}</td>
              <td className="py-2 px-4 text-green-600">{item.uploader}</td>
              <td className="py-2 px-4 text-red-600">{item.downloader}</td>
              <td className="py-2 px-4">{item.completed}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
