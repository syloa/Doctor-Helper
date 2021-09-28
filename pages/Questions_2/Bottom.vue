<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="뒤로"
        />
      </template>
      <template #title>Answer</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
        <div class="text-h5 q-mb-md">무엇이든 적어보ㅏ</div>

        <p v-for="i in 10" :key="i">12345</p>
      </div>
    </page-body>
  </page>
</template>

<script>
export default {
  name: 'Answer'
}
</script>
