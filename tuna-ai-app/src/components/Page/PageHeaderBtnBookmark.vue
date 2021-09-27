<template>
  <q-btn
    @click="useGoBack"
    icon="bookmark_border"
    color="primary"
    flat
    rounded
    dense
    no-caps
  />
</template>

<script>
import useGoBack from 'src/use/useGoBack'

export default {
  name: 'PageHeaderBtnBookmark',
  setup() {
    return {
      useGoBack
    }
  }
}
</script>