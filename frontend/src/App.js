import React, {Component, Fragment} from "react";
import Header from "./components/Header/Header";



class App extends Component{
    render(){
        return (<Fragment>
                 
                 <Header />
                 
                <div>
                    <li>
                        <a href="#"> PA</a>
                        <a href="#"> bs</a>
                    </li>
                </div>
                 
               </Fragment>)
    }
}


export default App;