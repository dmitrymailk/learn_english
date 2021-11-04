import axios from "axios";
import store from "../store/index";
// import router from "../router";

var apiServer = axios.create({
  baseURL: "http://127.0.0.1:8000/",

  crossdomain: true,
});

var staticFiles = axios.create({
  baseURL: "url for static files",
});

apiServer.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error) {
    if (401 === error.response.status) {
      store.dispatch("AUTH_LOGOUT");
      // router.push("/login");
      // console.log("UNAUTH");
      return Promise.reject(error);
    } else {
      return Promise.reject(error);
    }
  }
);

const token = localStorage.getItem("access");
if (token) {
  apiServer.defaults.headers.authorization = `Bearer ${token}`;
}
export { apiServer, staticFiles };
