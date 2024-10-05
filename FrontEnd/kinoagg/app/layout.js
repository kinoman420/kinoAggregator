import '../styles/global.css';
import React from 'react';

const RootLayout = ({ children }) => {
  return (
    <html lang="en">
      <head>
        <title>Kino Aggregator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
};

export default RootLayout;
