<template>
  <div id="q-app">
    <transition
      appear
      enter-active-class="animated fadeIn"
      leave-active-class="animated fadeOut"
      mode="out-in"
    >
      <router-view />
    </transition>
    <div v-if="loading" style="position:absolute; width: 100%; height:100%; top:0; left:0; z-index:10000; background-color:white">
        <div style="margin-left: auto; margin-right: auto">
            <splash />
        </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
// import Splash from './components/Splashs/Splash';
import Splash from './components/Splashs/Splash';

export default defineComponent({
  name: 'App',
  components: {
    Splash
  },
  data: () => ({
   loading: true
  }),
  mounted() {
    setTimeout(() => {
        this.loading = false
    }, 1000)
  }
})
</script>


<style>
/* 폰트 적용 */
body{ font-family: 'Noto Sans KR', 'sans-serif'; }
</style>
