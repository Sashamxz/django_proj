import React, {Component, Fragment} from "react";
import {  Routes,  Route } from "react-router-dom";
import Header from "./components/Header/Header";
import Login from "./components/Account/Login";
import { loadUser } from './actions/auth'
import useToken from './components/Account/useToken';
import {Link} from 'react-router-dom';


//check jwt token
const token = localStorage.getItem("token");
if (token) {
    setAuthToken(token);
}

const App = () => {
 
  
    
        return (
        <Fragment>
                 
                 
              <Header />
         <div>
                <Routes>
          
                 <Route path='/signup' element={<Login/>} />
                 <Link to="/signup" className="btn btn-warning">Register</Link>
                </Routes>
         </div>
                 
            </Fragment>)
    }



export default App;