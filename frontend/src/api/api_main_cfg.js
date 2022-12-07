import axios from 'axios';
import {store} from '../store/store'

const BASE_URL = 'http://127.0.0.1:8000/';

const defaultOptions = {
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
};

let instance = axios.create(defaultOptions);

instance.interceptors.request.use(function (config) {
  let token = store.getState()['auth'].token
  
  if (token !== undefined){
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export default instance;