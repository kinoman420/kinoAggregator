import { useState } from 'react';

const SortButton = ({ onSort }) => {
  const [sortCategory, setSortCategory] = useState('');

  const handleSort = (category) => {
    setSortCategory(category);
    onSort(category);
  };

  return (
    <div>
      <button onClick={() => handleSort('All')}>All</button>
      <button onClick={() => handleSort('Games')}>Games</button>
      <button onClick={() => handleSort('Movies')}>Movies</button>
      <button onClick={() => handleSort('Anime')}>Anime</button>
    </div>
  );
};

export default SortButton;