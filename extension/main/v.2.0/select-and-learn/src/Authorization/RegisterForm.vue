<template lang="pug">
.landing-page__auth
  p
    .landing-page__form-error(v-for="item in errors")
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
    button.btn.btn-primary(@click="register")
      |Register
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
    register(e) {
      e.preventDefault();
      this.errors = [];
      const { username, password } = this;
      this.$store
        .dispatch("REGISTER_REQUEST", { username, password })
        .then(() => {
          this.$router.push("/");
        })
        .catch((res) => {
          console.log("ERROR", res.response);
          let { password, username } = res.response.data;
          console.log(password, username);
          if (password) {
            this.errors = [...this.errors, ...password];
          }
          if (username) {
            this.errors = [...this.errors, ...username];
          }
        });
    },
  },
};
</script>
