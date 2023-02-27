import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';


const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="btn-group">
        <Link to="/products">Products</Link>
        <Link to="/customers">Customers</Link>
        <Link to="/orders">Orders</Link>
      </div>
    </div>
  );
}

export default Sidebar;
