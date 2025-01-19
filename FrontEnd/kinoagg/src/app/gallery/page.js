'use client'
import React, { useState, useEffect } from 'react';

export default function ImagesPage() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/media/images')
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        
        if (Array.isArray(data.images)) {
          const imagesWithData = data.images.map(filename => ({
            title: get_title_from_filename(filename),
            url: `http://localhost:8000/uploads/${filename}`
            
          }));
          setImages(imagesWithData);
        } else {
          console.error('Expected an array but got:', data.images);
        }
      })
      .catch(err => console.error(err));
  }, []);

  function get_title_from_filename(filename) {
    let title = filename.replace(/\[.*?\]/g, '').trim();
    title = title.replace(/^\W+|\W+$/g, '');
    return title;
  }

  return (
    <div>
      <h1>Uploaded Images</h1>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        {images.map((image) => (
          <div key={image.url} style={{ marginBottom: '20px' }}>
            <h3>{image.title}</h3>
            <img src={image.url} alt={image.title} style={{ maxWidth: '200px', height: 'auto' }} />
          </div>
        ))}
      </div>
    </div>
  );
}