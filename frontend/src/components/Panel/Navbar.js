import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";



function Navbar({ token, setToken }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    setToken("");
    navigate("/");
  };

  return (
    <div className="navBar">
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
        </ul>
        <ul className="ml-auto">
        <li>
          {token ? (
            <button onClick={handleLogout}>Logout</button>
          ) : (
            <Link to="/login">Login</Link>
          )}
        </li>
        <li>
          {!token && <Link to="/register">Register</Link>}
        </li>
        </ul>
      
    </nav>
    </div>
  );
}

export default Navbar;