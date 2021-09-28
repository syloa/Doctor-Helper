<template>
    <q-img
      src="../../assets/images/splash.png"
      :ratio="16/9"
      no-default-spinner
      img-class="filter"
      class="fixed-full bg-image"
    />
</template>
<script>
export default {
    name: 'Splash',
}
</script>
<style lang="scss">
.bg-image {
  // z-index: -1;
  height: 100%;
  opacity: 0.8;
  filter: brightness(0.9);
}
</style>