import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
Vue.config.productionTip = false;
import "./assets/style/index_extension.css";

const token = localStorage.getItem("access");
if (token) {
  axios.defaults.headers.common["Authorization"] = `$Bearer ${token}`;
}

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
