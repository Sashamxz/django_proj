import React, {Component, Fragment} from "react";
import { ReactDOM } from "react-dom";

import Header from "./layout/Header";
import CustomersList from "./layout/CustomerList";

class App extends Component{
    render(){
        return (<Fragment>
            <Header />
            <CustomersList />

        </Fragment>)
    }
}
