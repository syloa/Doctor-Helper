<template>
  <q-btn
    @click="goHome"
    icon="home"
    color="primary"
    flat
    rounded
    dense
    no-caps
  />
</template>
// import할때는 router로 보내야함
<script>
import { useRouter } from 'vue-router'

export default {
  name: 'PageHeaderBtnHome',
  setup() {
    const $router = useRouter()
// 내장함수로 쓰겠다 = $
    function goHome() {
      $router.push('/home') // 히스토리가 쌓인다 (저장O (뒤로가기 가능)
 
      // $router.replace('/home') // 히스토리가 안쌓이는것 가면서 해당 페이지 refresh,
      // $router.go('/home') 
      // 스택쌓임. -1을쓰면 뒤로한칸 그냥1쓰면 앞으로 한칸(히스토리가 쌓였을 때)
    }

    return {
      goHome
    }
  }
}
</script>