<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="Top"
        />
      </template>
      <template #title>Bottom2</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
        <div class="text-h5 q-mb-md">안ㄴㄴㄴ</div>

        <p v-for="i in 20" :key="i">ㄴㄴ</p>
      </div>
    </page-body>
  </page>
</template>

<script>
export default {
  name: 'Bottom'
}
</script>
