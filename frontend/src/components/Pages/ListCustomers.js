
import React from 'react';
import axios from 'axios';
import "./ListCustomers.css"


// // 'name', phone  email  description
class ListCustomers extends React.Component{
  state = {
    customers: []
  }

  componentDidMount() {
    const token = localStorage.getItem('token');
    axios.get('http://127.0.0.1:8000/api/v1/customers/', {
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then(res => {
      const customers = res.data;
      this.setState({ customers });
    })
    .catch(err => {
      console.log(err);
    });
  }

  render() {
 
    return ( <div className="list_customers" style={{ zIndex: 10 }}>
        <h1>Customers:</h1>
         <table className="table table-striped">
           <thead>
            <tr>
              <th>Name</th>
              <th>Phone</th>
              <th>Email</th>
              <th>Description</th>
              
              
           </tr>
         </thead>
         <tbody>
        {this.state.customers?.map(customer=> (
              <tr key={customer.id}>
                <td>{customer.name}</td>
                <td>{customer.phone}</td>
                <td>{customer.email}</td>
                <td>{customer.description}</td>
                 
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      );
    }
  }



export default ListCustomers;