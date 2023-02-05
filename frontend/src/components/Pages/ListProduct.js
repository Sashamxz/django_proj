
import React from 'react';
import axios from 'axios';
import deleteProduct from '../../actions/product'



// // 'name', 'price','category', 'description'




export  class ListProduct extends React.Component {
  state = {
    products: []
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/products')
      .then(res => {
        const products = res.data;
        this.setState({ products });
      })
  }

  render() {
 
    return ( <div className="list_products">
        <h1>Products:</h1>
         <table className="table table-striped">
           <thead>
            <tr>
              <th>Name</th>
              <th>Price</th>
              <th>Category</th>
              <th>Description</th>
              <th></th>
              
           </tr>
         </thead>
         <tbody>
        {this.state.products?.map(product=> (
              <tr key={product.id}>
                <td>{product.name}</td>
                <td>{product.price}</td>
                <td>{product.category}</td>
                <td>{product.description}</td>
                 
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      );
    }
  }







export default ListProduct;