<!-- 아이콘 이름은 https://fonts.google.com/icons에서 따온다. -->
<template>
  <q-btn
    @click="goHome"
    icon="chevron_left"
    color="primary"
    flat
    rounded
    dense
    no-caps
  />
</template>

<script>
import { useRouter } from 'vue-router'

export default {
  name: 'PageHeaderBtnHome',
  setup() {
    // $는 자바스크립트 내장 함수를 쓰겠다는 의미
    const $router = useRouter()
    function goHome() {
    $router.push('/home') // 히스토리가 쌓임 -> 뒤로가기 가능
    // $router.replace('/home') 히스토리가 쌓이지 않음
    // $router.go('/home') 해당 페이지로 이동하면서, 리프레시
    }
    return {
      goHome
    }
  }
}
</script>