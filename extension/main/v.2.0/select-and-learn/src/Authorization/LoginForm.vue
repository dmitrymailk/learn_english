<template lang="pug">
.landing-page__auth
  p
    .alert.alert-warning(v-for="item in errors")
      |{{item}}
  form
    .mb-3
      label.form-label
        |Username
      input.form-control(type="email" v-model="username")
    .mb-3
      label.form-label
        |Password
      input.form-control(type="password" v-model="password")
    button.btn.btn-primary(@click="login")
      |Login
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    login(e) {
      e.preventDefault();
      const { username, password } = this;
      this.errors = [];
      this.$store
        .dispatch("AUTH_REQUEST", { username, password })
        .then(() => {
          this.$router.push("/");
        })
        .catch((res) => {
          console.log("ERROR", res.response);
          let { password, username, detail } = res.response.data;
          console.log(password, username, detail);
          if (password) {
            this.errors = [...this.errors, ...password];
          }
          if (username) {
            this.errors = [...this.errors, ...username];
          }
          if (detail) {
            this.errors = [...this.errors, detail];
          }
        });
    },
  },
};
</script>
<style lang="sass">
.landing-page__auth
  font-family: Rubik
</style>
