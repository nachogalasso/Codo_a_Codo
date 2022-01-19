<template>
  <form action="#" class="gradient_form">
      <label for="linear">Linear
          <input type="radio" name="linear_grad" id="linear" value="linear" v-model="picked">
      </label>
      <label for="radial">Radial
          <input type="radio" name="radial_grad" id="radial" value="radial" v-model="picked">
      </label>
      <label for="conic">Conic
          <input type="radio" name="conic_grad" id="conic" value="conic" v-model="picked">
      </label>
  </form>
</template>

<script>
export default {
    data: () => ({
        picked: []
    }),

}

</script>

<style scoped>

.gradient_form {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 1.5rem 0;
}

label {
    font-size: 1.4rem;
    font-weight: 700;
}

input {
    margin: 0 .5rem;
}

</style>