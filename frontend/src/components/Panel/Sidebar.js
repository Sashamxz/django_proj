import React, { useState } from 'react';
import './Sidebar.css';





const Sidebar = () => {
  return (
      <div className='sidebar'>
          <h3>Sidebar</h3>
          
            <button onClick={() => navigateTo('products')}>Products</button> 
            <button onClick={() => navigateTo('customers')}>Customers</button>
            <button onClick={() => navigateTo('orders')}>Orders</button>
          
      </div>
  );
}

export default Sidebar;
