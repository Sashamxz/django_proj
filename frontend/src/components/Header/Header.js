import React, { Component } from 'react'
import './Header.css';


class Header extends Component {
  render() {
    return (
      <div className="header">
        <nav>
          <ul className="list">
            <li className="items">Home</li>
            <li className="items">Services</li>
            <li className="items">Contact</li>
          </ul>


          <div className="btn">
            <button className={HeaderCss.ButtonLogin} >
              {/* onClick={handleShowLogin} * */}
              Login
            </button>
            <button className="btn">
              {/* onClick={handleShowRegister} */}
              Register
            </button>
          </div>


        </nav>

      </div>
    )
  }
}

export default Header;