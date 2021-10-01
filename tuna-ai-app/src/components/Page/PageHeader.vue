<template>
  <header
    class="page-header q-header q-layout__section--marginal fixed-top q-header--bordered absolute-top bg-white text-dark"
  >
    <div class="q-toolbar row no-wrap items-center">
      <slot name="buttons-left" />
      <slot name="buttons-home" />
      <div class="page-header-title q-toolbar__title ellipsis text-body1 q-pl-none">
        <b><slot name="title" /></b>
        </div>
        <q-space></q-space><slot name="buttons-right" /><slot name="buttons-menu" />
      

    </div>
  </header>
</template>

<script>
export default {
  name: 'PageHeader'
}
</script>