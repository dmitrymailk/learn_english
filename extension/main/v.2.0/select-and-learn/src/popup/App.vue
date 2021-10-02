<template lang="pug">
.app
  .add-text
    .add-text__title(v-if="textTokens.length")
      |Your selected text:
    .add-text__text(v-if="textTokens.length")
      span.add-text__text-token(
        v-for="item in textTokens"
        @click="addToken(item)"
        )
        |{{item}} 
    .add-text__title(v-if="getSelectedTokens.length")
      |Your selected tokens:
    .add-text__text(v-if="getSelectedTokens.length")
      span.add-text__text-token(v-for="item in getSelectedTokens")
        span.add-text__text-token(
        v-for="item in textTokens"
        @click="deleteToken(item)"
        )
        |{{item}} 
        

   



</template>

<script>
export default {
  data() {
    return {
      textTokens: [],
      selectedTokens: new Set([]),
      getSelectedTokens: [],
    };
  },
  mounted() {
    this.getSelectedText();
  },
  methods: {
    addToken(token) {
      token = token.toLowerCase();
      // debugger;
      this.counter += 1;
      this.selectedTokens.add(token);
      console.log(this.getSelectedTokens, token, [...this.selectedTokens]);
      this.getSelectedTokens = [...this.selectedTokens];
    },
    getSelectedText() {
      console.log(window, window.chrome);
      window.chrome.storage.local.get("selectedText", (storage) => {
        if (storage["selectedText"]) {
          console.log(storage["selectedText"]);
          let text = storage["selectedText"].split(" ");
          this.textTokens = text;
        } else {
          console.log("no selected text");
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
