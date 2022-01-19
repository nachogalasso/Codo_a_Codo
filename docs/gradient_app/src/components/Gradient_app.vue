<template>
  <main>
    <section class="container">
    
      <section class="main_container">
        <h1>{{title}}</h1>
        <color></color>
        <gradient></gradient>
        <property></property>
      </section>

    </section>
    
  </main>
</template>

<script>
import Color from "./Colors.vue";
import Gradient from "./Gradient.vue";
import Property from "./Property.vue";

export default {

  components: {
    Color,
    Gradient,
    Property,
  },

  data: () => ({
    title: 'gradient generator',

  }),

  
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
    #db0059 5%,
    #aa2b87 10%,
    #684892 15%,
    #334e7d 20%,
    #2f4858 25%);
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
</style>
