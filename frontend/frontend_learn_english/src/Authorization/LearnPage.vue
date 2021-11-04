<template lang="pug">
  ul
    li(v-for="card in cards")
      |{{card.sentence}}
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
  created() {
    apiServer({ url: "select-learn/words-all/", method: "GET" }).then((res) => {
      console.log(res);
    });
  },
};
</script>
