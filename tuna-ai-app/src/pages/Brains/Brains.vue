<template>
  <page>
    <page-header>
      <template #buttons-home>
        <page-header-btn-home
          label="홈"
        />
      </template>
      <template #title>뇌 CT</template>
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
          <q-tab name="진단 대기" label="진단 대기" />
          <q-tab name="진단 완료" label="진단 완료" />
        </q-tabs>
        <q-separator />
        <q-tab-panels v-model="tab" >
          <q-tab-panel name="진단 대기">
            <div class="row">
              <router-link
          v-for="image in brainList.filter(image => image.detect === false)"
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
          </q-tab-panel>

          <q-tab-panel name="진단 완료">
            <div class="row">
              <router-link
          v-for="image in brainList.filter(image => image.detect === true)"
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
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
      </div>


   <!-- <q-btn color="black" text-color="black" label="Standard" @click="getBrainList" /> -->
    </page-body>
  </page>

</template>

<script>
import { onActivated, onDeactivated, onUpdated, ref, reactive } from 'vue'
import { axios, apiDB } from 'boot/axios'
import { useQuasar } from 'quasar'
import DBs from 'src/doctorStore/MongoDB.js'

export default {
  name: 'Brains',
  setup() {
    var brainList = ref([])

    const $q = useQuasar()
    const tab = ref('진단 대기')

    // function getBrainList() {
    //   var config = {
    //     method: 'get',
    //     url: '/brain',
    //     headers: { }
    //   };



    // // apiDB(config)
    // // .then(function (response) {
    // //   console.log('response', response)
    // //   console.log('response.data', response.data)
    // //   console.log('response.data.data', response.data.data)
    // //   // console.log(JSON.stringify(response.data));
    // //   // brainList.value = response.data.data
      
    // // })
    // // .catch(function (error) {
    // //   // 처리 오류의 경우 화면에 notice
    // //   console.log(error);
      
    // // });
    // }

    onActivated(() => {
      getBrains()
      console.log(brainList)
    })

    onUpdated(() => {
      getBrains()
    })

    onDeactivated(() => {
    })

        
    async function getBrains() {
      try{
        brainList.value =  await DBs.getList('brain') 
        console.log('성공', brainList.value[0].url)
      } catch (e) {
        console.log('error', e)
      }    
      
    }



    // function saveLocal(){
    //   $q.localStorage.set(1, "테스트")
    // }

    // function getLocal() {
    //   const value = $q.localStorage.getItem(1)
    //   console.log("불러오기", value)
    // }

    function count() {
      var cnt = 0
      for (const obj in brainList.value) {
        if (brainList.value[obj]["detect"] === false) {
          cnt = cnt +1
        }
      }
      return cnt
    }

    return {
     
      slide: ref(1),
      // saveLocal,
      // getLocal,
      // getBrainList,
      tab,
      brainList,
      count
    }
  }
}
</script>
