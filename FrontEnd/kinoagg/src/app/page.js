'use client';
import { useEffect, useState } from 'react';
import Card from './components/card';
import { roboto_mono } from './ui/font';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};

export default function Home() {
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState('');
  const [sortCategory, setSortCategory] = useState('All'); // Default to 'All'
  const [isDropdownOpen, setIsDropdownOpen] = useState(false); // Declare isDropdownOpen state
  const debouncedQuery = useDebounce(query, 300);

  const [username, setUsername] = useState(null);
  const [isAdmin, setIsAdmin] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const storedUsername = localStorage.getItem('username');
    const storedIsAdmin = localStorage.getItem('is_admin') === 'true';
    
    if (storedUsername) {
      setUsername(storedUsername);
      setIsAdmin(storedIsAdmin);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('is_admin');
    setUsername(null);
    setIsAdmin(false);
    router.push('/');
  };

  const handleUsernameClick = () => {
    if (isAdmin) {
      router.push('/admin-dashboard'); 
    } else {
      router.push('/user-dashboard'); 
    }
  };

  useEffect(() => {
    if (debouncedQuery) {
      fetchItems(debouncedQuery, sortCategory);
    }
  }, [debouncedQuery, sortCategory]);

  // Mapping of categories to API endpoints
  const endpointMapping = {
    'All': '/search/',
    'Game': '/game/',
    'Movies': '/searchmovie/',
    'Anime': '/anime/'
  };

  const fetchItems = async (searchQuery, category) => {
    try {
      const endpoint = endpointMapping[category] || '/search/';
      console.log('Fetching from:', `http://localhost:8000${endpoint}?what=${searchQuery}`);
      const response = await fetch(`http://localhost:8000${endpoint}?what=${searchQuery}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      console.log('Fetched data:', data);
      setItems(data[0]);  
    } catch (error) {
      console.error('Failed to fetch data:', error);
    }
  };

  const handleSearch = (event) => {
    event.preventDefault();
    fetchItems(query, sortCategory);
  };

  const handleSortChange = (category) => {
    setSortCategory(category);
    setIsDropdownOpen(false); // Close dropdown after selection
  };

  return (
    <div className={`container ${roboto_mono.className}`}>
      <header className="flex justify-between items-center px-4">
        {/* Left Section */}
        <div className="flex items-center">
          <h1 className="text-3xl font-bold mr-4">Kaggregator</h1>
          <Link href="/gallery" className={`text-lg font-medium text-blue-500 ${roboto_mono.className}`}>
            Gallery
          </Link>
        </div>
        {username ? (
          <>
            <span onClick={handleUsernameClick} style={{ cursor: 'pointer' }} className="text-black">
              {username}
            </span>
            <button onClick={handleLogout} className="text-black ml-2">
              Logout
            </button>
          </>
        ) : (
          <h2 className="text-3xl font-bold">
            <Link href="/login" className="text-black">
              Login
            </Link>
          </h2>
        )}

        <form onSubmit={handleSearch} className="flex items-center">
          {/* Custom Dropdown */}
          <div className="relative mr-2">
            <button
              type="button"
              onClick={() => setIsDropdownOpen(!isDropdownOpen)}
              className={`border rounded px-6 py-2 text-black bg-white hover:bg-gray-100 focus:outline-none w-40 ${roboto_mono.className}`}
            >
              {sortCategory || 'Sort by'}
            </button>
            {isDropdownOpen && (
              <ul className="absolute mt-1 w-40 bg-white border rounded shadow-lg z-10">
                <li
                  onClick={() => handleSortChange('All')}
                  className={`px-4 py-2 hover:bg-gray-100 cursor-pointer text-black ${roboto_mono.className}`}
                >
                  All
                </li>
                <li
                  onClick={() => handleSortChange('Game')}
                  className={`px-4 py-2 hover:bg-gray-100 cursor-pointer text-black ${roboto_mono.className}`}
                >
                  Game
                </li>
                <li
                  onClick={() => handleSortChange('Movies')}
                  className={`px-4 py-2 hover:bg-gray-100 cursor-pointer text-black ${roboto_mono.className}`}
                >
                  Movies
                </li>
                <li
                  onClick={() => handleSortChange('Anime')}
                  className={`px-4 py-2 hover:bg-gray-100 cursor-pointer text-black ${roboto_mono.className}`}
                >
                  Anime
                </li>
              </ul>
            )}
          </div>

          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search"
            className={`border rounded px-4 py-2 mr-2 text-black ${roboto_mono.className}`}
          />
          <button
            type="submit"
            className={`bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 ${roboto_mono.className}`}
          >
            Search
          </button>
        </form>
      </header>
      <div className="bg-white">
        {items.map((item, index) => (
          <Card key={index} item={item} />
        ))}
      </div>
    </div>
  );
}