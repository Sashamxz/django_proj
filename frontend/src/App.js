import React, {Component, Fragment} from "react";
import Header from "./components/Header";
import ListProduct from "./components/ListProduct";


class App extends Component{
    render(){
        return (<Fragment>
                 
                 <Header />
                 
                 <ListProduct />
                 
               </Fragment>)
    }
}


export default App;