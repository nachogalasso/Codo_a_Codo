<template>
<!-- COLOR FORM -->
  <form action="#" class="color_form">
      <!-- 1st COLOR -->
      <section class="colors">
          <label for="color">C1:
              <input type="color" name="fcolor" id="color" v-model="fcolor">
          </label>
          <label for="deg">{{degrees}}
              <input type="number" name="deg" id="deg" min="0" max="100" v-model="fstop">
          </label>
          <p class="text">HEX1: {{fcolor}}</p>
      </section>
      <!-- 2nd COLOR -->
      <section class="colors">
          <label for="color">C2:
              <input type="color" name="scolor" id="color" v-model="scolor">
          </label>
          <label for="deg">{{degrees}}
              <input type="number" name="deg" id="deg" min="0" max="100" v-model="sstop">
          </label>
          <p class="text">HEX1: {{scolor}}</p>
      </section>
  </form>
</template>

<script>

export default {
    data: () => ({
        fcolor: '#000000',
        scolor: '#ea0606',
        fstop: 0,
        sstop: 0,
        degrees: '%:',
    }),

}
</script>

<style scoped>

.colors {
    display: flex;
    align-items: center;
    justify-content: space-around;
    margin: 1rem 0;
    width: 100%;
}

.colors label,
.text {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 .5rem;
}

input[type="color"] {
    border: none;
    padding: 0;
    background: inherit;
}

input[type="number"] {
    border-radius: .5rem;
    border: .2rem solid #000;
}
</style>