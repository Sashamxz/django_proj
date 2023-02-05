import { Routes, Route } from "react-router-dom";
import "./App.css";

// Pages Imports
import ListProduct from "./components/Pages/ListProduct";
import Login from "./components/Account/Login" ;
import Register from "./components/Account/Register";

// Component Imports
import Navbar from "./components/Panel/Navbar";
import Footer from "./components/Panel/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <ListProduct />
            </PrivateRoute>
          }
        />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;