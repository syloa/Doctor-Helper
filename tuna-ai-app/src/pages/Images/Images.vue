<template>
  <page>
    <page-header>
      <template #title>갤러리</template>
    </page-header>
    <page-body>
      <div class="row">
        <router-link
          v-for="image in store.state.images"
          :key="image.id"
          :to="`/images/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          />
        </router-link>
      </div>
    </page-body>
  </page>
</template>

<script>
import store from 'src/myStore'

export default {
  name: 'Images',
  setup() {
    return {
      store
    }
  }
}
</script>
