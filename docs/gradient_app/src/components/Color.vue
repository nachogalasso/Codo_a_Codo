<template>
  <section class="colors">
              <label for="color">C1:
                  <input type="color" name="fcolor" id="color" v-model="fcolor">
              </label>
              <label for="deg">%:
                  <input type="number" name="deg" id="deg" min="0" max="100" v-model="fstop">
              </label>
              <p class="text">HEX1: {{fcolor}}</p>
          </section>
</template>

<script>
export default {

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