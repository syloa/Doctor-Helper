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
import { defineComponent , ref} from 'vue';
import Splash from './components/Splashs/Splash';
import { LocalStorage, useQuasar, setCssVar, getCssVar } from 'quasar'
import { useI18n } from 'vue-i18n'

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
    }, 3000)
  },
  // 최초 진입점 -> 조건문 or try/catch문으로 localDB에 필요한 것 저장 혹은 불러오기
  setup() {
    const $q = useQuasar()
    
    const { locale } = useI18n({ useScope: 'global' })
    
    // 색 기본 설정 localDB에 저장
    try{
      setCssVar('primary', $q.localStorage.getItem('primary'))
      } catch (e) {
        $q.localStorage.set('primary', getCssVar('primary'))
        console.log('error', e)
      }
    //  언어 기본 설정 localDB에 저장
     try{
      if ($q.localStorage.getItem('language') == null) {
          $q.localStorage.set('language', 'ko')
      }
      locale.value = $q.localStorage.getItem('language')
      
      } catch (e) {
        console.log('error', e)
      }  
  }
  
})
</script>


<style>
/* 폰트 적용 */
body{ font-family: 'Noto Sans KR', 'sans-serif'; }
</style>