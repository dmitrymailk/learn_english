<template lang="pug">

.authorization
  .authorization__left
    .authorization__brand-name
      |Lingvo Gap
    .authorization__img
      img(src="https://lingvo-gap.com/static-files/landing/login.svg", alt="alt")
  .authorization__right
    router-link(to="/login").authorization__switch-button
      |Login
    .authorization__title
      |Register
    RegisterForm
</template>

<script>
import RegisterForm from "./RegisterForm";

export default {
  components: {
    RegisterForm,
  },
};
</script>

<style lang="sass">
.authorization
  display: flex
  height: 100%
  width: 100%
  &__left
    display: flex
    height: 100%
    width: 35%
    background: #222222
    align-items: center
    justify-content: center
    position: relative
  &__img
    width: 320px
    height: 192px
    img
      height: 100%
      width: 100%
  &__brand-name
    position: absolute
    top: 32px
    left: 32px
    font-family: Rubik
    font-style: normal
    font-weight: bold
    font-size: 33px
    line-height: 39px
    color: #FFFFFF
  &__right
    display: flex
    flex-direction: column
    width: 65%
    align-items: center
    justify-content: center
    background: #fdfdff
  &__switch-button
    border: 2px solid #222222
    box-sizing: border-box
    border-radius: 8px
    width: 160px
    height: 48px
    font-family: Rubik
    font-style: normal
    font-weight: bold
    font-size: 18px
    line-height: 21px
    color: #222222
    cursor: pointer
    display: flex
    align-items: center
    justify-content: center
    position: absolute
    top: 32px
    right: 32px
  &__title
    font-family: Rubik
    font-style: normal
    font-weight: bold
    font-size: 35px
@media (max-width: 1024px)
  .authorization
    display: flex
    height: 100%
    width: 100%
    &__left
      display: flex
      height: 100%
      width: 35%
    &__img
      width: 80%
    &__brand-name
      position: absolute
      top: 16px
      left: 16px
      font-size: 26px
      color: #FFFFFF
    &__right
      width: 65%
      align-items: center
      justify-content: center
    &__switch-button
      width: 140px
      height: 40px
      font-size: 16px
      line-height: 21px
      position: absolute
      top: 16px
      right: 16px
    &__title
      font-size: 28px
@media (max-width: 519px)
  .authorization
    flex-direction: column
    padding-bottom: 100px
    &__left
      height: 220px
      width: 100%
    &__img
      width: 60%
    &__brand-name
      position: absolute
      top: 8px
      left: 8px
      font-size: 20px
      color: #FFFFFF
    &__right
      width: 100%
      margin-top: 16px
      align-items: center
      justify-content: center
    &__switch-button
      width: 120px
      height: 40px
      font-size: 14px
      border: 2px solid #ffffff
      color: #ffffff
      top: 8px
      right: 8px
    &__title
      font-size: 24px
</style>
