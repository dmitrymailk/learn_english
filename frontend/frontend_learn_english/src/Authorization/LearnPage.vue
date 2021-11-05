<template lang="pug">
.app
  .card.w-50.mx-auto.learn-card
    .card-body
      p.card-text
        | {{cards[stage].sentence}}
      input.form-control
      .button-container
        a.btn.btn-secondary.mt-3(href="#")
          |Next
      .synonyms-list
        span.synonyms-list__title
          |Synonyms:
        span.synonyms-list__synonym(v-for="item in synonyms" )
          |{{item}},
</template>

<script>
import { apiServer } from "../utils/api";

export default {
  data() {
    return {
      stage: 0,
      cards: [],
    };
  },
  computed: {
    sentence: function () {
      if (this.card.length > 0) return this.cards[this.stage].sentence;
      return "";
    },
    synonyms: function () {
      if (this.card.length > 0) return this.cards[this.stage].synonyms;
      return [];
    },
  },
  created() {
    apiServer({ url: "select-learn/words-all/", method: "GET" }).then((res) => {
      console.log(res);

      const { sentences, words } = res.data;
      let cards = [];
      let mappedSentences = {};
      sentences.forEach((element) => {
        mappedSentences[element.sentence_id] = element.sentence_text;
      });

      words.forEach((element) => {
        let card = {};
        let sentence = mappedSentences[element.sentence_id];
        let word = element.word;
        sentence = sentence.replace(word, "_____");
        card["sentence"] = sentence;
        card["word"] = word;
        card["synonyms"] = element.synonyms;
        cards.push(card);
      });

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
  // right: 0px
  // position: relative
</style>
