<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label=""
        />
      </template>
      <template #title>{{ $t('title_bookmark') }}</template>
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
          v-for="image in chestList.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/xrays/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
               {{$t("detect_caption")}}{{ image.caption}}
            </div>
          </q-img>
        </router-link>
        </div>
      
      <div 
      v-if='preferred==="Brain"'
      class="row">
        <router-link
          v-for="image in brainList.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/brains/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
              {{$t("detect_caption")}}{{ image.caption}}
            </div>
          </q-img>
        </router-link>
      </div>

      <div
      v-if='preferred==="Skin"'
      class="row">
        <router-link
          v-for="image in skinList.filter(image => image.bookmark === true)"
          :key="image.id"
          :to="`/skins/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
               {{$t("detect_caption")}}{{ image.caption}}
            </div>
          </q-img>
        </router-link>
      </div>
    

      </div>
    </page-body>
  </page>
</template>

<script>
import { onActivated, onDeactivated, onUpdated, ref } from 'vue'
import DBs from 'src/doctorStore/MongoDB.js'

export default {
name: 'Bookmarks',
data() {
    let label_chest = ref("")
    let label_brain = ref("")
    let label_skin = ref("")
    onActivated(() => {
      label_chest.value = this.$t("title_chests")
      label_brain.value = this.$t("title_brains")
      label_skin.value = this.$t("title_skins")
    })
    onUpdated(() => {
      label_chest.value = this.$t("title_chests")
      label_brain.value = this.$t("title_brains")
      label_skin.value = this.$t("title_skins")
    })
    return {
      options: [
      {
        label: label_chest,
        value: 'Chest'
      },
      {
        label: label_brain,
        value: 'Brain'
      },
      {
        label: label_skin,
        value: 'Skin'
      }
    ],
    }
  },


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

  var chestList = ref([])
  var brainList = ref([])
  var skinList = ref([])

  onActivated(() => {
      getValues()
    })
    
  async function getValues() {
    try{
      chestList.value =  await DBs.getList('chest') 
      brainList.value =  await DBs.getList('brain') 
      skinList.value =  await DBs.getList('skin') 
    } catch (e) {
      console.log('error', e)
    }    

  }

  return {
    preferred: ref('Chest'),
    // options: [
    //   {
    //     label: '흉부 X-ray',
    //     value: 'Chest'
    //   },
    //   {
    //     label: '뇌 CT',
    //     value: 'Brain'
    //   },
    //   {
    //     label: '피부 이미지',
    //     value: 'Skin'
    //   }
    // ],
    onSubmit,
    chestList,
    skinList,
    brainList
  }
}
}
</script>