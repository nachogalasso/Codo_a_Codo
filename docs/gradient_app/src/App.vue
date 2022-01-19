<template>
  <div id="app">
    <gradient-app></gradient-app>
  </div>
</template>

<script>

import GradientApp from "./components/Gradient_app.vue"

export default {
  name: 'App',
  components: {
    GradientApp
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;700&display=swap');

html {
  font-size: 62.5%;
  box-sizing: border-box;
  font-family: 'Ubuntu', Arial, Helvetica, sans-serif;
}

html::-webkit-scrollbar {
    display: none;
}

html:focus-within {
    scroll-behavior: smooth;
}

*, *:before, *:after {
    box-sizing: inherit;
}

body {
  margin: 0;
  padding: 0;
  height: 100hv;
}

</style>
