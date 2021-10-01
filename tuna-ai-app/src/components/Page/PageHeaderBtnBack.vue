<template>
  <q-btn
    @click="Back"
    icon="chevron_left"
    color="primary"
    flat
    rounded
    dense
    no-caps
  />
</template>

<script>
import useGoBack from 'src/use/useGoBack'
import { useRouter } from 'vue-router'

export default {
  name: 'PageHeaderBtnBack',
  setup() {
    const $router = useRouter()
    

    function Back(){
      $router.go(-1)
    }


    return {
      Back,
    }
  }
}
</script>