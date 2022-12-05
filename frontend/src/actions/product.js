import {GET_PRODUCT, DELETE_PRODUCT, ADD_PRODUCT, GET_ERRORS} from './types';



// GET Product

export const getProduct = () => (dispatch, getState) => {
    Axios.get("/api/products/", tokenConfig(getState))
      .then((res) =>
        dispatch({
          type: GET_PRODUCT,
          payload: res.data,
        })
      )
      .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
  };
  
//   // DELETE Product
  
  export const deleteProduct = (id) => (dispatch, getState) => {
    Axios.delete(`/api/products/${id}/`, tokenConfig(getState))
      .then((res) => {
        dispatch(createMessage({ deleteLead: "Product Deleted" }));
        dispatch({
          type: DELETE_LEAD,
          payload: id,
        });
      })
      .catch((err) => console.log(err));
  };
  
//   // ADD Product
  
//   export const addProduct = (lead) => (dispatch, getState) => {
//     Axios.post("/api/products/", lead, tokenConfig(getState))
//       .then((res) => {
//         dispatch(createMessage({ addLead: "Product Added" }));
//         dispatch({
//           type: ADD_LEAD,
//           payload: res.data,
//         });
//       })
//       .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
//   };