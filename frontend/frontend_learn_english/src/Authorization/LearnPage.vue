<template lang="pug">
.app
  .card.learn-card.mx-2.mt-3
    .card-body.px-3(v-show="learningStatus == 0")
      .card-text
        a.card-text__item(v-for="word in sentence" target="_blank" :href="word.link")
          | {{word.word}}
      input.form-control.mt-2(
        v-model="userInput" 
        :placeholder="wordTip"  
        @keyup="setInputStatus" 
        v-bind:class="setInputClass"
        ref="input"
      )
      .button-container
        a.btn.btn-secondary.mt-3.next-button(@click="applyCard")
          |Next
      .definitions-list.mt-3
        span.definitions-list__title
          |POS: 
        span {{posDefinition}}
      .definitions-list
        span.definitions-list__title
          |Definitions: 
        ul 
         li(v-for="item in definitions")
          | {{item}}
    h3.mt-5.mb-5.text-center.px-5(v-show="learningStatus == 1")
      |No more cards on server 
    h3.mt-5.mb-5.mr-3.text-center.px-5(v-show="learningStatus == 2")
      span.loading-text
        |Saving Progress...
      .spinner-border.text-dark(role="status")
    h3.mt-5.mb-5.text-center.px-5(v-show="learningStatus == 3")
      span.loading-text
        |Loading cards...
      .spinner-border.text-dark(role="status")
    audio(ref="audioElement")

    
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
      learningStatus: 0,
    };
  },
  computed: {
    sentence: function () {
      if (this.cards.length > 0) {
        // console.log(
        //   this.cards[this.stage].sentence,
        //   this.cards[this.stage].sentence.split(" ")
        // );
        let sentence = this.cards[this.stage].sentence.split(" ");
        let newSentence = [];
        sentence.forEach((word) => {
          newSentence.push({
            link: `https://www.google.com/search?tbm=isch&q=${word}`,
            word: word,
          });
        });
        return newSentence;
      }
      return [];
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
  mounted() {
    this.getNewCards();
    // refs не работают если использовать диррективу v-if
    console.log();
  },
  methods: {
    startAudio() {
      console.log(this.$refs.audioElement.duration);
      this.$refs.audioElement.play();
    },

    async nextStage() {
      if (this.cardsIndexes.length > 1) {
        console.log("next 1");
        this.cardsIndexes.shift();
        this.stage = this.cardsIndexes[0];
        this.$refs.input.focus();
      } else if (this.nextCardsIndexes.length > 0) {
        console.log("next 2");
        this.cardsIndexes = arrayShuffle(this.nextCardsIndexes);
        this.nextCardsIndexes = [];
        this.stage = this.cardsIndexes[0];
        this.$refs.input.focus();
      } else {
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
        // console.log("Cards saved");
      } catch (err) {
        console.log("ERROR", err);
      }
    },
    async getNewCards() {
      apiServer({ url: "select-learn/words-all/", method: "GET" }).then((res) => {
        // console.log(res);

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
          // не работает...
          // this.$refs.input.focus();
        } else {
          this.learningStatus = 1;
        }
      });
    },
    setInputStatus(e) {
      this.inputStatus = 0;
      if (e.keyCode === 13) {
        this.applyCard();
      }
    },
    async applyCard() {
      let userInput = this.userInput;
      const stage = this.stage;
      userInput = userInput.toLowerCase().replace(/\s+/g, "");

      let correctAnswer = this.cards[this.stage].word;
      correctAnswer = correctAnswer.toLowerCase().replace(/\s+/g, "");

      this.$refs.audioElement.src = this.cards[this.stage]["sound_link"];
      if (userInput === correctAnswer) {
        this.inputStatus = 1;
        if (this.cards[stage]["sound_link"].length > 0) {
          this.$refs.audioElement.play();

          const nextCard = () => {
            this.userInput = "";
            this.inputStatus = 0;
            this.nextStage();
            this.$refs.audioElement.removeEventListener("ended", nextCard);
          };

          this.$refs.audioElement.addEventListener("ended", nextCard);
        } else {
          setTimeout(() => {
            this.userInput = "";
            this.inputStatus = 0;
            this.nextStage();
          }, 400);
        }
      } else {
        this.inputStatus = 2;
        this.userInput = "";
        this.wordTip = correctAnswer;
        this.nextCardsIndexes.push(stage);
        this.cards[stage].errors += 1;

        this.$refs.audioElement.play();
        const errorTip = () => {
          this.wordTip = "";
          this.inputStatus = 0;
          this.$refs.audioElement.removeEventListener("ended", errorTip);
        };
        this.$refs.audioElement.addEventListener("ended", errorTip);
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

.learn-card
  max-width: 600px

.loading-text
  margin-right: 20px

.card-text
  display: inline-flex
  flex-wrap: wrap
  &__item
    text-decoration: none
    color: #222
    margin-right: 5px
    // word-wrap: normal


@media (max-width: 652px)
  .app
    align-items: flex-start
  .learn-card
    margin: 0 8px
</style>
