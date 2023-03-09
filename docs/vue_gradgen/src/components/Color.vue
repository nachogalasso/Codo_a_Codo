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
    class CreateColor {
		constructor(id, color, deg) {
			this.id=id;
			this.color=color;
			this.deg=deg;
		}
	}
    
    const newColor = new CreateColor(id, color, deg)
    const newColorChange = Object.entries(newColor)
    console.log(newColorChange)
    // colorStore.colorPair.push({...newColor})

    console.log(colorStore.colorPair)

    // addColors()
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