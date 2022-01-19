<template>
  <form action="#" class="bck_form">
      <label for="ort">Orientation:
          <input type="number" name="ort" id="ort" min="0" max="360" v-model="orientation">
      </label>
      <label for="prop">Property:
          <input type="text" name="prop" id="prop">
      </label>
  </form>
</template>

<script>
export default {
    data: () => ({
        orientation: 0,
    })

}
</script>

<style>

</style>