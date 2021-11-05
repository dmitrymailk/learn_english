<template lang="pug">
.app
  .card.w-50.mx-auto.learn-card
    .card-body
      p.card-text
        | {{sentence}}
      input.form-control
      .button-container
        a.btn.btn-secondary.mt-3(href="#")
          |Next
      .definitions-list
        span.definitions-list__title
          |Definitions: 
        ul 
         li(v-for="item in definitions")
          | {{item}}
      .definitions-list
        span.definitions-list__title
          |POS Definition: 
        span {{posDefinition}}
</template>

<script>
import { apiServer } from "../utils/api";
// import axios from "axios";
export default {
  data() {
    return {
      stage: 0,
      cards: [],
    };
  },
  computed: {
    sentence: function () {
      if (this.cards.length > 0) return this.cards[this.stage].sentence;
      return "";
    },
    definitions: function () {
      if (this.cards.length > 0) {
        if (this.cards[this.stage].definition.length > 0)
          return this.cards[this.stage].definition;
        return ["No word definitions"];
      }
      return ["No word definitions"];
    },
    posDefinition: function () {
      if (this.cards.length > 0) {
        return this.cards[this.stage].pos_definition;
      }
      return "No pos definition.";
    },
  },
  created() {
    apiServer({ url: "select-learn/words-all/", method: "GET" }).then((res) => {
      console.log(res);

      const cards = res.data;

      this.cards = cards;
    });
  },
};
</script>

<style lang="sass">
body, html
  display: flex
  height: 100% !important
  width: 100% !important

.app
  height: 100%
  width: 100%
  display: flex
  align-items: center
  justify-content: center

.button-container
  display: flex
  justify-content: flex-end

.next-button
  width: 100px

.definitions-list
  &__title
    font-weight: bold
</style>
