<template lang="pug">
.landing-page__auth
  p
    .landing-page__form-error(v-for="item in errors")
      |{{item}}
  .landing-page__form
    .landing-page__form-title
      |Username
    input.landing-page__form-input(type="email" v-model="username")
  .landing-page__form
    .landing-page__form-title
      |Password
    input.landing-page__form-input(type="password" v-model="password")
  button.landing-page__register(@click="login")
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
    login() {
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
