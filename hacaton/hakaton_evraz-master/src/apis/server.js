import axios from 'axios';


export default axios.create({
  baseURL: `http://127.0.0.1:8000`,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
  },
});
