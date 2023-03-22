<template>
  <form action="" class="color-container"  >
    <section class="colors">
        <label for="lcolor">Color:
            <input type="color" name="lcolor" id="" v-model="color">
        </label>
        <label for="deg" class="deg_label">%:
            <input type="number" name="deg" id="deg" min="0" max="100" v-model="deg" @change.prevent="addColors()">
        </label>
        <p class="text">HEX: {{color}}</p>
    </section>
  </form>
</template>

<script setup>
import {ref} from "vue";
import { colorStore} from "../store/store.js"

let color = ref("#rrggbb");
let deg = ref(0);
let id = ref(crypto.randomUUID())

function addColors() {
    colorStore.colorPair.push({
        id: crypto.randomUUID(),
        color: color.value,
        deg: deg.value,
    })
    console.log(colorStore.colorPair)
}
    
</script>

<style scoped>
.color-container {
    width: 100%;
}

.colors {
    display: flex;
    align-items: center;
    justify-content: space-around;
}

</style>