import React, {Component, Fragment} from "react";
import {  Routes,  Route } from "react-router-dom";
import Header from "./components/Header/Header";
import Login from "./components/Account/Login";
import { loadUser } from './actions/auth'
import useToken from './components/Account/useToken';
import {Link} from 'react-router-dom';



const App = () => {
 
    const { token, setToken } = useToken();
    
    if(!token) {
            return <Login setToken={setToken} />
          }
      
    
    
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