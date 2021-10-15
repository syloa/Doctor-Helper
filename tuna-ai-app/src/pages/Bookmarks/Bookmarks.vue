<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label=""
        />
      </template>
      <template #title>북마크</template>
      <template #buttons-menu>
        <page-header-btn-menu
        />
      </template>
    </page-header>
    <page-body>
      <div class="q-pa-md">
      <div class="bg-grey-2 q-pa-sm rounded-borders">
        <q-option-group
          name="preferred_genre"
          v-model="preferred"
          :options="options"
          color="primary"
          inline
        />
      </div>
      <div 
      v-if='preferred==="Chest"'
      class="row">
        <router-link
          v-for="image in storeChest.state.images.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/xrays/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
              {{ image.caption}}
            </div>
          </q-img>
        </router-link>
        </div>
      
      <div 
      v-if='preferred==="Chest"'
      class="row">
        <router-link
          v-for="image in storeBrain.state.images.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/brains/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
              {{ image.caption}}
            </div>
          </q-img>
        </router-link>
      </div>

      <div
      v-if='preferred==="Skin"'
      class="row">
        <router-link
          v-for="image in storeSkin.state.images.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/skins/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
              {{ image.caption}}
            </div>
          </q-img>
        </router-link>
      </div>
    

      </div>
    </page-body>
  </page>
</template>

<script>
import { ref } from 'vue'
import storeBrain from 'src/doctorStore/brain.js'
import storeChest from 'src/doctorStore/xray.js'
import storeSkin from 'src/doctorStore/skin.js'
export default {
name: 'Bookmarks',
setup () {
  const submitResult = ref([])
  function onSubmit (evt) {
      const formData = new FormData(evt.target)
      const data = []
      for (const [ name, value ] of formData.entries()) {
        data.push({
          name,
          value
        })
      }
      submitResult.value = data
    }
  return {
    preferred: ref('Chest'),
    options: [
      {
        label: '흉부 X-ray',
        value: 'Chest'
      },
      {
        label: '뇌 CT',
        value: 'Brain'
      },
      {
        label: '피부 이미지',
        value: 'Skin'
      }
    ],
    onSubmit,
    storeBrain,
    storeChest,
    storeSkin
  }
}
}
</script>