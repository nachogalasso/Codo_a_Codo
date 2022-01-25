<template>
  <section class="btn">
    <button title="Add Color">
      <i class="far fa-plus-square"></i>
    </button>
  </section>
</template>

<script>
import NewColor from "./Color.vue";

export default {
  components: {
    NewColor,
  },

  

}

</script>

<style scoped>
@import url("https://use.fontawesome.com/releases/v5.15.4/css/all.css");

.far {
  position: absolute;
  font-size: 1.5rem;
  font-weight: 700;
  cursor: pointer;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

button {
  position: relative;
  width: 2.5rem;
  height: 2.5rem;
  margin-left: 2.5rem;
  border-radius: 50%;
  border: none;
  background-color: rgba(10, 129, 10, 0.5);
}

</style>