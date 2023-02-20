// App.js

import React, { useState, useEffect } from "react";
import ListProduct from "./components/Pages/ListProduct";
import Login from "./components/Account/Login" ;
import Register from "./components/Account/Register";
import { getToken, removeToken } from './actions/auth';


import Navbar from "./components/Panel/Navbar";
import Footer from "./components/Panel/Footer";
import Sidebar from "./components/Panel/Sidebar";


function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    const token = getToken();
    if (token) {
      setLoggedIn(true);
    }
  }, []);

  function handleLogout() {
    removeToken();
    setLoggedIn(false);
  }

  return (
    <div className="App">
      <Navbar loggedIn={loggedIn} handleLogout={handleLogout} />
   
      {loggedIn ? (
        <button onClick={handleLogout}>Logout</button>
      ) : (
        <>
          <Login setLoggedIn={setLoggedIn} />
          <Register />
        </>
      )}
      <Sidebar />
      <ListProduct />
      <Footer />
    </div>
  );
}

export default App;
