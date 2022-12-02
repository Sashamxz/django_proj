import React, { Component, Fragment } from "react";
// import { connect } from "react-redux";
// import PropTypes from "prop-types";
import { getProduct } from "../actions/product";




export class ListProduct extends Component {
  // static propTypes = {
  //   products: PropTypes.array.isRequired,
  //   getProduct: PropTypes.func.isRequired,
  //   deleteProduct: PropTypes.func.isRequired,
  // };

  componentDidMount() {
    this.props.getProduct();
  }

// 'name', 'price','category', 'description'
  render() {
    return ( <div className="list_products">
       <h1>Products</h1>
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
            {this.props.products.map((product) => (
              <tr key={product.id}>
                <td>{product.name}</td>
                <td>{product.price}</td>
                <td>{product.category}</td>
                <td>{product.description}</td>
                <td>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={this.props.deleteProduct.bind(this, product.id)}
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
};

// const mapStateToProps = (state) => ({
//   products: state.products.products,
// });

export default ListProduct;