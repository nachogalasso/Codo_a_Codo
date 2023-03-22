<script setup>
import Color from "./components/Color.vue";

const title = "gradient generator";



function addOtherColor() {
  const newColor = document.querySelector('.colors-container');
  newColor.append(Color)
}


</script>

<template>
<!-- GRADIENT CONTAINER START -->
  <main class="grad__container">

    <!-- APP FUNCTION CONTAINER START -->
    <section class="main__container">
      <h1 class="main__container-title">{{title}}</h1>
        <Color />
        <Color />
      
    </section>
    <!-- APP FUNCTION CONTAINER END -->

  </main>
<!-- GRADIENT CONTAINER END -->
</template>

<style scoped>
.main__container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  border: .1rem solid #000;
  border-radius: 1rem;
  background-color: rgba(224, 226, 219, .1);
  backdrop-filter: blur(2.2rem);
  -webkit-backdrop-filter: blur(2.2rem);
  box-shadow: .5rem .5rem 2rem #fff;
}

.main__container-title {
  font-size: 2.5rem;
  font-variant: small-caps;
  margin: 1rem 0;
}

.grad__container {
  
  width: 90vw;
  max-width: 65rem;
}

</style>
