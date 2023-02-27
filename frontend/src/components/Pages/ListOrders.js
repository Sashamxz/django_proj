
import React from 'react';
import axios from 'axios';
import "./ListOrders.css"


//  customer product status usrgency


class  ListOrders extends React.Component  {
  state = {
    orders: []
  }

  componentDidMount() {
    const token = localStorage.getItem('token');

    axios.get('http://127.0.0.1:8000/api/v1/orders/', {
      headers: {
        'Authorization': 'Bearer ' + token
      }
    }).then(res => {
      const orders = res.data;
      this.setState({ orders });
    })
    .catch(err => {
      console.log(err);
    });
  }


  render() {
 
    return ( <div className="list_orders" style={{ zIndex: 10 }}>
        <h1>Orders:</h1>
         <table className="table table-striped">
           <thead>
            <tr>
              <th>Customer</th>
              <th>Product</th>
              <th>Status</th>
              <th>Urgency</th>
              <th>Date</th>
              
           </tr>
         </thead>
         <tbody>
        {this.state.orders?.map(order=> (
              <tr key={order.id}>
                <td>{order.customer}</td>
                <td>{order.product}</td>
                <td>{order.status}</td>
                <td>{order.urgency}</td>
                <td>{order.data_created}</td>
                 
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      );
    }
  }


export default ListOrders;