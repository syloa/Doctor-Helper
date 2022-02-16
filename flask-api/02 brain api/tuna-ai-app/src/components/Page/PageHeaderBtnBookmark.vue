<template>
  <q-btn
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
import {ref} from 'vue'

export default {
  name: 'PageHeaderBtnBookmark',
  setup() {
    const $router = useRouter()
    const bookmarkicon = ref(false)

    function bookmark () {
      bookmarkicon.value = !bookmarkicon.value
      console.log(bookmarkicon.value)
    }

    
    return {
      useGoBack,
      bookmark,
      bookmarkicon
    }
  }
}
</script>