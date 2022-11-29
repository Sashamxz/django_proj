import React, {Component, Fragment} from "react";
import Header from "./components/Header";
import NavbarW from "./components/Navbar";

class App extends Component{
    render(){
        return (<Fragment>
                 <NavbarW />
                 <Header />
                 <Home />
               </Fragment>)
    }
}


export default App;