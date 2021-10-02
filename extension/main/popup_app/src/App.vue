<template lang="pug">
.app
  .add-text
    .add-text__title
      |Your selected text:
    .add-text__text
      span.add-text__text-token(
        v-for="item in textTokens"
        @click="()=>addToken(item)"
        )
        |{{item}}
    .add-text__title(v-if="selectedTokens.size")
      |Your selected tokens:
    .add-text__text(v-if="selectedTokens.size")
      span.add-text__text-token(v-for="item in getSelectedTokens")
        |{{item}},



</template>

<script>
// import { onMounted } from "vue";

export default {
  data() {
    return {
      textTokens: ["Some", "test", "tokens", "for", "test"],
      selectedTokens: new Set([]),
    };
  },
  computed: {
    getSelectedTokens() {
      return Array.from(this.selectedTokens);
    },
  },

  mounted() {
    // console.log(window, window.chrome.storage);
    this.getSelectedText();
  },
  methods: {
    addToken(token) {
      token = token.toLowerCase();
      this.selectedTokens.add(token);
    },
    getSelectedText() {
      console.log(window, window.chrome);
      window.chrome.storage.local.get("selectedText", (storage) => {
        if (storage["selectedText"]) {
          console.log(storage["selectedText"]);
        }
      });
    },
  },
  name: "App",
};
</script>

<style lang="sass">
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&display=swap')
html, body, #app
  margin: 0
  height: 300px
  width: 450px
  font-family: 'Nunito', sans-serif

.app
  height: 100%
  width: 100%
  display: flex
  border: 1px solid black
  flex-direction: column

.add-text
  &__title
    font-size: 18px
    font-weight: 600
  &__text
    font-size: 16px
    &-token
      display: inline-flex
      align-items: center
      justify-content: center
      margin: 2px
      margin-right: 2px
      &:hover
        background: rgba(0, 0, 0, 0.1)
        cursor: pointer
        border-radius: 4px
</style>
