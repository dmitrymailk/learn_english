import Vue from "vue";
import VueRouter from "vue-router";
import MyPlugin from "./MenuPlugin";

import Authorization from "../Authorization/Authorization.vue";
import LearnPage from "../Authorization/LearnPage.vue";

Vue.use(VueRouter);
Vue.use(MyPlugin);

const routes = [
  {
    path: "/login",
    component: Authorization,
  },
  {
    path: "/",
    component: LearnPage,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

import store from "./../store/index";

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  store.commit("UPDATE_LINK", from.fullPath);

  const publicPages = ["/login"];
  const isPrivatePage = !publicPages.includes(to.path);
  if (isPrivatePage) {
    if (store.getters.isAuthenticated) {
      // set link for next usage
      next();
      return;
    }
    next("/login");
    store.commit("AUTH_ERROR");
  } else {
    next();
  }
});

export default router;
