<template>
  <section class="colors">
      <label for="lcolor" class="label_color">C1:
          <input type="color" name="color" id="lcolor" class="icolor" v-model="fcolor">
      </label>
      <label for="deg" class="deg_label">%:
          <input type="number" name="deg" id="deg" min="0" max="0" v-model="fstop">
      </label>
      <p class="text">HEX 1: {{fcolor}}</p>
   </section>
</template>

<script>
export default {
   name: "FColor",
}
</script>

<style scoped>

.colors {
    display: flex;
    align-items: center;
    margin: 1rem 0;
}

.label_color {
    font-size: 1.5rem;
    font-weight: 700;
}

.deg_label {
    font-size: 1.5rem;
    font-weight: 700;
    padding-left: .5rem;
}

.icolor {
    border: none;
    /* border-radius: 50%; */
    padding: 0;
    background: inherit;
}

.text {
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0;
    padding-left: .5rem;
}

</style>