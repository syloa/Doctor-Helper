<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>피부 이미지</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>
    <page-body>
        <div class="q-gutter-y-md" style="max-width: 600px">
        <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="진단 대기" label="진단 대기" />
          <q-tab name="진단 완료" label="진단 완료" />
        </q-tabs>
        <q-separator />
        <q-tab-panels v-model="tab" >
          <q-tab-panel name="진단 대기">
            <div class="row">
              <router-link
          v-for="image in storeSkin.state.images.filter(image => image.predbool === false)"
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
          </q-tab-panel>

          <q-tab-panel name="진단 완료">
            <div class="row">
              <router-link
          v-for="image in storeSkin.state.images.filter(image => image.predbool === true)"
          :key="image.id"
          :to="`/skins/${ image.id }`"
          class="col-6"
        >
          <q-img
            :src="image.url"
            :ratio="1"
          >
            <div class="absolute-top text-center">
              {{ image.caption}}}
            </div>
          </q-img>
        </router-link>

            </div>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
      </div>

    <!-- <div class="q-pa-md">
      <q-carousel
        animated
        v-model="slide"
        arrows
        navigation
        infinite
      >
        <q-carousel-slide :name="1" img-src="http://localhost:8085/images/xrays/1.jpg" />
        <q-carousel-slide :name="2" img-src="http://localhost:8085/images/xrays/2.png" />
        <q-carousel-slide :name="3" img-src="http://localhost:8085/images/xrays/3.png" />
        <q-carousel-slide :name="4" img-src="http://localhost:8085/images/xrays/4.png" />
      </q-carousel>
    </div> -->



    <!-- <div>
      <div class="q-pa-sm">
        <q-btn color="white" text-color="black" label="Standard" @click="saveLocal" />
        <q-btn color="deep-orange" glossy label="Deep Orange" @click="getLocal"/>
      </div>
      <br>
    </div> -->
<!--     
      <div class="row">
        <router-link
          v-for="image in store.state.images"
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
      </div> -->


    </page-body>
  </page>
</template>

<script>
import storeSkin from 'src/doctorStore/skin.js'
import { ref } from 'vue'
import { useQuasar } from 'quasar'

export default {
  name: 'Skins',
  setup() {
    const $q = useQuasar()
    const tab = ref('진단 대기')

    function saveLocal(){
      $q.localStorage.set(1, "테스트")
    }

    function getLocal() {
      const value = $q.localStorage.getItem(1)
      console.log("불러오기", value)
    }

    return {
      storeSkin,
      slide: ref(1),
      saveLocal,
      getLocal,
      tab: ref('진단 대기')
    }
  }
}
</script>
