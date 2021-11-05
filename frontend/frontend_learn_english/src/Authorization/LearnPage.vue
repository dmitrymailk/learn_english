<template lang="pug">
.app
  .card.w-50.mx-auto.learn-card
    .card-body(v-if="learningStatus == 0")
      p.card-text
        | {{sentence}}
      input.form-control(
        v-model="userInput" 
        :placeholder="wordTip"  
        @keyup="setInputStatus" 
        v-bind:class="setInputClass"
      )
      .button-container
        a.btn.btn-secondary.mt-3.next-button(@click="applyCard")
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
    h3.mt-5.mb-5.text-center(v-else-if="learningStatus == 1")
      |No more cards on server 
    h3.mt-5.mb-5.mr-3.text-center(v-else-if="learningStatus == 2")
      span.loading-text
        |Saving Progress...
      .spinner-border.text-dark(role="status")
    h3.mt-5.mb-5.text-center(v-else-if="learningStatus == 3")
      span.loading-text
        |Loading cards...
      .spinner-border.text-dark(role="status")

    
</template>

<script>
import { apiServer } from "../utils/api";
import arrayShuffle from "../utils/arrayOperation";
// import axios from "axios";
export default {
  data() {
    return {
      stage: 0,
      cards: [],
      cardsIndexes: [],
      nextCardsIndexes: [],
      wordTip: "",
      inputStatus: 0,
      userInput: "",
      learningStatus: 3,
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
    setInputClass: function () {
      switch (this.inputStatus) {
        case 0:
          return "";
        case 1:
          return "is-valid";
        case 2:
          return "is-invalid";
      }
      return "";
    },
  },
  created() {
    this.getNewCards();
  },
  methods: {
    async nextStage() {
      if (this.cardsIndexes.length > 1) {
        console.log("GENERAL STAGE");
        this.cardsIndexes.shift();
        this.stage = this.cardsIndexes[0];
      } else if (this.nextCardsIndexes.length > 0) {
        console.log("NEXT StAGE");
        this.cardsIndexes = arrayShuffle(this.nextCardsIndexes);
        this.nextCardsIndexes = [];
        this.stage = this.cardsIndexes[0];
      } else {
        console.log("END REPETITION");
        console.log("SAVING ANSWERS");
        await this.saveCards();
        this.learningStatus = 3;
        await this.getNewCards();
      }
    },
    async saveCards() {
      this.learningStatus = 2;

      try {
        let words = [];
        this.cards.forEach((card) => {
          let word = {};
          if (card.errors == 0) {
            word["strength"] = Math.min(card["strength"] + 1, 6);
          } else if (card.errors <= 2) {
            word["strength"] = Math.max(card["strength"] - 1, 1);
          } else {
            word["strength"] = 1;
          }
          word["word_id"] = card["word_id"];
          words.push(word);
        });

        await apiServer({
          url: "select-learn/words-all/",
          method: "PUT",
          data: words,
        });
        console.log("Cards saved");
      } catch (err) {
        console.log("ERROR", err);
      }
    },
    async getNewCards() {
      apiServer({ url: "select-learn/words-all/", method: "GET" }).then((res) => {
        console.log(res);

        let cards = res.data;
        let cardsIndexes = [];
        for (let i = 0; i < cards.length; i++) {
          cards[i]["errors"] = 0;
          cardsIndexes.push(i);
        }

        this.cards = cards;
        this.cardsIndexes = cardsIndexes;
        if (this.cards.length > 0) {
          this.learningStatus = 0;
          this.stage = 0;
        } else this.learningStatus = 1;
      });
    },
    setInputStatus(e) {
      this.inputStatus = 0;
      if (e.keyCode === 13) {
        this.applyCard();
      }
    },
    applyCard() {
      let userInput = this.userInput;
      const stage = this.stage;
      userInput = userInput.toLowerCase().replace(/\s+/g, "");

      let correctAnswer = this.cards[this.stage].word;
      correctAnswer = correctAnswer.toLowerCase().replace(/\s+/g, "");

      console.log(userInput, correctAnswer, stage);
      if (userInput === correctAnswer) {
        this.inputStatus = 1;
        setTimeout(() => {
          this.userInput = "";
          this.inputStatus = 0;
          this.nextStage();
        }, 400);
      } else {
        this.inputStatus = 2;
        this.userInput = "";
        this.wordTip = correctAnswer;
        this.nextCardsIndexes.push(stage);
        this.cards[stage].errors += 1;
        let timeout = 1000;
        if (this.cards[stage].errors >= 4) timeout = 2000;

        setTimeout(() => {
          this.wordTip = "";
          this.inputStatus = 0;
        }, timeout);
      }
    },
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

.loading-text
  margin-right: 20px
</style>
