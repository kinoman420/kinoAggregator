
import React from 'react';
import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-black text-white p-4 flex justify-between items-center">
        <div className="flex items-center space-x-4">
        <div className="text-2xl font-bold">
            Kaggregator
        </div>
        <div className="flex space-x-4">
            <Link href="/lists"  className="hover:underline">
            My Lists
            </Link>
            <Link href="/info" className="hover:underline">
            Info
            </Link>
        </div>
        </div>
      
      <div className="flex items-center space-x-2">
        <select className="bg-gray-800 text-white p-2 rounded">
          <option value="all">All</option>
          <option value="Anime">Anime</option>
          <option value="Games">Games</option>
          <option value="Movies">Movies</option>
          {/* Add more options here */}
        </select>
        <input 
          type="text" 
          placeholder="search for torrent" 
          className="p-2 rounded text-black"
        />
        <button className="bg-blue-600 p-2 rounded">
          <img src="search-icon.svg" alt="Search" className="h-4 w-4" />
        </button>
        <div className="flex items-center space-x-2">
            <button>
            <img src="/person.svg" alt="User" className="h-6 w-6" />
            <img src="/dropdown.svg" alt="Dropdown" className="h-4 w-4" />
            </button>
          
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
