
import React from 'react';
import axios from 'axios';
import deleteProduct from '../actions/product'



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
    // return ( <div> 
    // <h2>Products list</h2>
    //   <ul>
    //     { this.state.products?.map(product=> <li>{product.name}</li>)}
    //   </ul>
    //   </div> 
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
                <td>
                <button
                    className="btn btn-danger btn-sm"
                    onClick={this.state.deleteProduct.bind(this, lead.id)}
                  >
                    Delete
                </button>
                </td>  
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      );
    }
  }







// export class ListProduct extends Component {
//   // static propTypes = {
//   //   products: PropTypes.array.isRequired,
//   //   getProduct: PropTypes.func.isRequired,
//   //   deleteProduct: PropTypes.func.isRequired,
//   // };

//   componentDidMount() {
//     this.props.getProduct();
//   }







//   render() {
//     return ( <div className="list_products">
//        <h1>Products</h1>
//         <table className="table table-striped">
//           <thead>
//             <tr>
//               <th>Name</th>
//               <th>Price</th>
//               <th>Category</th>
//               <th>Description</th>
//               <th></th>
//             </tr>
//           </thead>
//           <tbody>
//             {this.props.products.map((product) => (
//               <tr key={product.id}>
//                 <td>{product.name}</td>
//                 <td>{product.price}</td>
//                 <td>{product.category}</td>
//                 <td>{product.description}</td>
//                 <td>
//                   <button
//                     className="btn btn-danger btn-sm"
//                     onClick={this.props.deleteProduct.bind(this, product.id)}
//                   >
//                     Delete
//                   </button>
//                 </td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//         </div>
     
//     );
//   }
// };

// const mapStateToProps = (state) => ({
//   products: state.products.products,
// });

export default ListProduct;