<template>
  <page>
    <page-header>
      <template #buttons-home>
        <page-header-btn-home
          label="Home"
        />
      </template>
      <template #title >뇌 CT</template>
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
    
      <div class="row">
        <router-link
          v-for="image in store.state.images"
          :key="image.id"
          :to="`/brains/${ image.id }`"
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


    </page-body>
  </page>
</template>

<script>
import store from 'src/doctorStore/brain.js'
import { ref } from 'vue'
import { useQuasar } from 'quasar'


export default {
  name: 'Brains',
  setup() {
    
    function saveLocal(){
      $q.localStorage.set(1, "테스트")
    }

    function getLocal() {
      const value = $q.localStorage.getItem(1)
      console.log("불러오기", value)
    }

    return {
      store,
      slide: ref(1),
      saveLocal,
      getLocal
    }
  }
}
</script>
