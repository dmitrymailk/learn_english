<template lang="pug">
.authorization.px-2
  .btn.btn-secondary(@click="switchType")
    |Switch
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
