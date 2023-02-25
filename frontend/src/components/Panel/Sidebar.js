import React, { useState } from 'react';
import './Sidebar.css';





const Sidebar = () => {
  return ( <div className="sidebar">
            <div class="btn-group">
          
            <button onClick={() => navigateTo('products')}>Products</button> 
            <button onClick={() => navigateTo('customers')}>Customers</button>
            <button onClick={() => navigateTo('orders')}>Orders</button>
          </div>
      </div>
  );
}

export default Sidebar;