import { useState } from "react";
import { Route, Routes } from "react-router-dom";
import "./App.css";



import Navbar from "./components/Panel/Navbar";
import Footer from "./components/Panel/Footer";
import Sidebar from "./components/Panel/Sidebar";

import Home from "./components/Pages/Home";
import About from "./components/Pages/About";

import Login from "./components/Accounts/Login" ;
import Register from "./components/Accounts/Register";




function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");

  const handleSetToken = (newToken) => {
    setToken(newToken);
    localStorage.setItem("token", newToken);
  };

  return (
    <div className="App">
      <Navbar token={token} setToken={handleSetToken} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/login"
          element={<Login token={token} setToken={handleSetToken} />}
        />
        <Route
          path="/register"
          element={<Register token={token} setToken={handleSetToken} />}
        />
      </Routes>
      <Sidebar />
      <Footer />
    </div>
  );
}

export default App;
