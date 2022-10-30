import axios from 'axios'

var API_URL = process.env.REACT_APP_API_URL;
const Api = axios.create({
  baseURL: API_URL
});

export default Api