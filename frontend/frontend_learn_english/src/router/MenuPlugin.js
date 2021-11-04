export default {
  install: function(Vue) {
    // Use Vue instance for plugin data
    // var store = new Vue({
    //   data: {
    //     scrollY: 0
    //   }
    // });
    // // Handle window scroll event
    // var timer = null;
    // window.addEventListener("scroll", function() {
    //   if (timer === null) {
    //     timer = setTimeout(function() {
    //       // Substitute for scrollY property at 200 ms intervals
    //       store.scrollY = window.scrollY;
    //       clearTimeout(timer);
    //       timer = null;
    //     }, 200);
    //   }
    // });

    // Register in the instance property
    Vue.prototype.$deleteMenu = function() {
      document.querySelector(".main-navbar").classList.add("none");
    };

    Vue.prototype.$showMenu = function() {
      document.querySelector(".main-navbar").classList.remove("none");
    };
  }
};
