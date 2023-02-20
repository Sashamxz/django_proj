// Navbar.js

import React from 'react';

function Navbar({ loggedIn, handleLogout }) {
  return (
    <nav>
      <ul>
        <li>My App</li>
        <li>Products</li>
        {loggedIn ? (
          <li onClick={handleLogout}>Logout</li>
        ) : (
          <>
            <li>Login</li>
            <li>Register</li>
          </>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
