'use client';
import { useEffect, useState } from 'react';
import Card from './components/card';
import { roboto_mono } from './ui/font';
import Link from 'next/link'

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
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (debouncedQuery) {
      fetchItems(debouncedQuery);
    }
  }, [debouncedQuery]);

  const fetchItems = async (searchQuery) => {
    try {
      const response = await fetch(`http://localhost:8000/search/?what=${searchQuery}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      console.log("Fetched data:", data);
      setItems(data[0]);  
    } catch (error) {
      console.error("Failed to fetch data:", error);
    }
  };

  const handleSearch = (event) => {
    event.preventDefault();
    fetchItems(query);
  };

  return (
    <div className={`container ${roboto_mono.className}`}>
      <header className="flex justify-between items-center  px-4">
        <h1 className="text-3xl font-bold">Kaggregator</h1>
        <h2 classname="text-3xl font-bold">
          <Link href="/login">Login</Link>
        </h2>
        <form onSubmit={handleSearch} className="flex items-center">
          <input 
            type="text" 
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search" 
            className="border rounded px-2 py-1 mr-2" 
          />
          <button 
            type="submit" 
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            Search
          </button>
        </form>
      </header>
      <div className='bg-white'>
        {items.map((item, index) => (
          <Card key={index} item={item} />
        ))}
      </div>
    </div>
  );
}
