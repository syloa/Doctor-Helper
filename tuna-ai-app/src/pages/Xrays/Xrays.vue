<template>
  <page>
    <page-header>
      <template #buttons-home>
        <page-header-btn-home
        />
      </template>
      <template #title>{{ $t('title_chest') }}</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>
    <page-body>
      
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
          <q-tab name="진단 대기" :label="$t('tab_btn_wait')" />
          <q-tab name="진단 완료" :label="$t('tab_btn_complete')" />
        </q-tabs>
        <q-separator />
        <q-tab-panels v-model="tab" >
          <q-tab-panel name="진단 대기">
            <div class="row">
              <router-link
          v-for="image in chestList.filter(image => image.detect === false)"
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
          </q-tab-panel>

          <q-tab-panel name="진단 완료">
            <div class="row">
              <router-link
          v-for="image in chestList.filter(image => image.detect === true)"
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
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
      </div>



    </page-body>
  </page>
</template>

<script>
// import storeXray from 'src/doctorStore/xray.js'
import { onActivated, onDeactivated, onUpdated, ref, reactive } from 'vue'
import { useQuasar } from 'quasar'
import { axios, apiDB } from 'boot/axios'
import DBs from 'src/doctorStore/MongoDB.js'

export default {
  name: 'Xrays',
  setup() {
    var chestList = ref([])

    const $q = useQuasar()
    const tab = ref('진단 대기')

    // function saveLocal(){
    //   $q.localStorage.set(1, "테스트")
    // }

    // function getLocal() {
    //   const value = $q.localStorage.getItem(1)
    //   console.log("불러오기", value)
    // }

    onActivated(() => {
      getXrays()
      console.log(chestList)
    })

    onUpdated(() => {
      getXrays()
    })

    onDeactivated(() => {
    })

        
    async function getXrays() {
      try{
        chestList.value =  await DBs.getList('chest') 
        console.log('성공', chestList.value[0].url)
      } catch (e) {
        console.log('error', e)
      }    
      
    }


    function count() {
      var cnt = 0
      for (const obj in chestList.value) {
          if (chestList.value[obj]["detect"] === false) {
          cnt = cnt +1
        }
      }
      return cnt
    }

    return {
      // storeXray,
      slide: ref(1),
      // saveLocal,
      // getLocal,
      tab,
      chestList
    }
  }
}
</script>
