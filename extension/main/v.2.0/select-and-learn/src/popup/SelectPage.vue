<template lang="pug">

.app
  .add-text.px-2(v-if="textTokens.length")
    h4
      |Your selected text:
    p.add-text__text
      span.add-text__text-token(
        v-for="item in textTokens"
        @click="addToken(item)"
        )
        |{{item}} 
    .add-text__title.font-weight-bold(v-if="getSelectedTokens.length")
      |Your selected words:
    .add-text__text(v-if="getSelectedTokens.length")
      span.add-text__text-token(
        v-for="item in getSelectedTokens"
        @click="deleteToken(item)")
        |{{item}},
    .server-button.mt-3(v-if="getSelectedTokens.length")
      button.btn.btn-primary.add-text__button.mr-3(@click="sendToServer" ) 
        |Send to server
      .spinner-border.text-dark.spinner-button(role="status" v-if="sendStatus == 1")
      span.badge.badge-success(role="status" v-else-if="sendStatus == 2") Ok
      span.badge.badge-danger(role="status" v-else-if="sendStatus == 3") Error

</template>

<script>
import "../assets/style/bootstrap.min.css";
import { apiServer } from "../utils/api";

export default {
  data() {
    return {
      originalText: "",
      textTokens: [],
      selectedTokens: new Set([]),
      getSelectedTokens: [],
      sendStatus: 0,
    };
  },
  mounted() {
    this.getSelectedText();
  },
  methods: {
    addToken(token) {
      token = token.toLowerCase();
      this.selectedTokens.add(token);
      this.getSelectedTokens = [...this.selectedTokens];
    },
    deleteToken(token) {
      token = token.toLowerCase();
      this.selectedTokens.delete(token);
      this.getSelectedTokens = [...this.selectedTokens];
    },
    getSelectedText() {
      console.log(window, window.chrome);
      window.chrome.storage.local.get("selectedText", (storage) => {
        if (storage["selectedText"]) {
          console.log(storage["selectedText"]);
          this.originalText = storage["selectedText"];
          this.textTokens = this.processTokens(storage["selectedText"].split(" "));
        } else {
          console.log("no selected text");
        }
      });
    },
    processTokens(tokens) {
      let processTokens = [];
      tokens.forEach((element) => {
        element = element.replace(/[^A-Za-z0-9\-]/g, "");
        processTokens.push(element);
      });
      return processTokens;
    },
    sendToServer() {
      console.log("SEND TO SERVER", this.originalText, [...this.selectedTokens]);
      const newWords = {
        sentence: this.originalText,
        words: [...this.selectedTokens],
      };
      this.sendStatus = 1;
      apiServer({
        url: "select-learn/add-words/",
        data: newWords,
        method: "POST",
      })
        .then((res) => {
          console.log("OK", res);
          this.sendStatus = 2;
        })
        .catch((rej) => {
          console.log("ERROR", rej);
          this.sendStatus = 3;
        });
    },
  },
  name: "App",
};
</script>

<style lang="sass">
html, body
  margin: 0
  min-height: 300px
  height: 100%
  width: 450px
  border-radius: 6px
  font-family: Arial, Helvetica, sans-serif

.app
  height: 100%
  width: 100%
  display: flex
  border: 1px solid black
  flex-direction: column

.add-text
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

.spinner-button
  height: 20px
  width: 20px
</style>
