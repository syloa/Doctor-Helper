<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="Top"
        />
      </template>
      <template #title>Bottom</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
        <div class="text-h5 q-mb-md">안알랴줌</div>

        <p v-for="i in 20" :key="i">메롱</p>
      </div>
    </page-body>
  </page>
</template>

<script>
export default {
  name: 'Bottom'
}
</script>
