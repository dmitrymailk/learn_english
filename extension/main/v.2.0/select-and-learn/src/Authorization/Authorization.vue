<template lang="pug">
.authorization
  .authorization__switch-button(@click="switchType")
    |Switch

  router-link(to="/")
    | to home 
  LoginForm(v-if="type == 'Login'")
  RegisterForm(v-else)
</template>

<script>
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";

export default {
  data() {
    return {
      type: "Login",
    };
  },
  methods: {
    switchType() {
      if (this.type == "Login") this.type = "Register";
      else this.type = "Login";
    },
  },
  computed: {
    switchedType: function () {
      let type = "";
      if (this.type == "Login") type = "Register";
      else type = "Login";
      return type;
    },
  },
  components: {
    LoginForm,
    RegisterForm,
  },
};
</script>

<style lang="sass">
.authorization
  &__switch-button
    border: 2px solid #222222
    box-sizing: border-box
    border-radius: 8px
    width: 160px
    height: 48px
    font-family: Arial, Helvetica, sans-serif
    font-style: normal
    font-weight: bold
    font-size: 18px
    line-height: 21px
    color: #222
    cursor: pointer
    display: flex
    align-items: center
    justify-content: center
</style>
