<template>
    <section class="container" :style="setColor">
    
      <section class="main_container">
        <h1>{{title}}</h1>
        <!-- COLOR FORM -->
        <form action="#" class="color_form">
      <!-- 1st COLOR -->
          <section class="colors">
              <label for="color">C1:
                  <input type="color" name="fcolor" id="color" v-model="fcolor">
              </label>
              <label for="deg">%:
                  <input type="number" name="deg" id="deg" min="0" max="100" v-model="fstop">
              </label>
              <p class="text">HEX1: {{fcolor}}</p>
          </section>
          <!-- 2nd COLOR -->
          <section class="colors">
              <label for="color">C2:
                  <input type="color" name="scolor" id="color" v-model="scolor">
              </label>
              <label for="deg">%:
                  <input type="number" name="deg" id="deg" min="0" max="100" v-model="sstop">
              </label>
              <p class="text">HEX1: {{scolor}}</p>
          </section>
          <btn></btn>
        </form>
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
        <form action="#" class="bck_form">
          <label for="ort" v-if="this.picked === 'linear'" class="show">Orientation:
              <input type="number" name="ort" id="ort" min="0" max="360" v-model="orientation">
          </label>
          <label for="prop">Property:
              <input type="text" name="prop" id="prop" :value="setColor">
          </label>
        </form>
      </section>
    </section>
    
</template>

<script>
import Btn from "./Button.vue"

export default {
  components: {
    Btn,
  },

  data: () => ({
    title: 'gradient generator',
    fcolor: '',
    fstop: 0,
    scolor: '',
    sstop: 0,
    picked: [],
    orientation: 0,
  }),

  mounted() {
        this.setColor()
    },

  computed: {
    setColor() {
      if(this.picked === 'linear'){
        return `background: ${this.picked}-gradient(${this.orientation}deg, ${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
      }else{
        return `background: ${this.picked}-gradient(${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
      }
    }
  }
  
}
</script>

<style scoped>

.container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main_container {
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

h1 {
  font-size: 3.2rem;
  font-variant: small-caps;
  margin: 0 0 1rem;
  background: linear-gradient(to right, 
    #ea0606 0%,
    #db0059 20%,
    #aa2b87 45%,
    #684892 66%,
    #334e7d 83%,
    #2f4858 95%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 400% 400%;
  animation: gradient 10s ease infinite alternate;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }

}

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

.gradient_form {
    display: flex;
    justify-content: space-around;
    margin: 1.5rem 0;
    width: 100%;
}

.bck_form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 1rem 0;
}

label {
    font-size: 1.3rem;
    font-weight: 700;
}

input[type="text"] {
    margin: .5rem 0;
    padding: .5rem 1rem;
    width: 100%;
    border: .1rem solid #000000;
    border-radius: .5rem;
    box-shadow: .1rem .08rem .5rem #000000;
}

.show {
    display: block;
}

@media screen and (min-width: 768px) {
  .main_container {
    width: 45%;
  }

  .color_form,
  .gradient_form {
    width: 95%;
  }

  .bck_form {
    padding: 0 2rem;
    width: 100%;
  }

  h1 {
    font-size: 4rem;
  }

  .colors label,
  .text,
  label {
    font-size: 1.6rem;
  }  
}
</style>
