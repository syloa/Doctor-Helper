<template>
  <page>
    <page-header>
 
      <template #buttons-left>
        <page-header-btn-back
          label=""
        />
             
      </template>
     
      <template #title>{{ $t('title_help') }}</template>
      <template #buttons-menu> <page-header-btn-menu />  </template>
      
    
    </page-header>
    <page-body>
      <div class="row justify-center">
      <q-img
              src="/images/profile/info.png"
              class="no-pointer-events row justify-center"
              no-transition
              no-spinner
              style="width:370px; height:270px; margin-top: 10px; border-radius: 10px"
              />
      </div>
      <div class="q-pa-lg" style="font-size: 17px" >
 <br> 
{{$t('info_main') }}

      <br> 


      </div>
    <!-- contents -->
     <div class="q-pa-md q-gutter-md">
    <q-list bordered padding class="rounded-borders" style="max-width: 380px">


      <q-item clickable v-ripple >
        <q-item-section avatar>
          <q-avatar icon="las la-x-ray" color="primary" text-color="white" />
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">{{$t('home_btn_chest') }}</q-item-label>
          <q-item-label caption> {{ $t('info_cap_chest1') }} <br>{{ $t('info_cap_chest2') }} </q-item-label>
        </q-item-section>

        <q-item-section side>
        <q-btn icon="chevron_right" flat size="18px"  text-color="primary" @click="popUp1">
      
    </q-btn>
          

    <q-dialog v-model="carousel1" full-height>
      <q-carousel
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        v-model="slide_chest"
        control-color="primary"
        navigation
        padding
        arrows
        class="bg-white shadow-1 rounded-borders"
      >
        <q-carousel-slide :name="1" class="column no-wrap flex-center" height="360px">
          <div class="q-mt-md text-center text-weight-bold" style="font-size: 17px">
            {{ $t('info_carousel_title') }}<br>
             </div>
            <div class="q-mt-md text-center">
            {{ $t('cd1') }}, {{ $t('cd2') }}, {{ $t('cd3') }}, {{ $t('cd4') }}, {{ $t('cd5') }}, {{ $t('cd6') }},
            {{ $t('cd7') }}, {{ $t('cd8') }}, {{ $t('cd9') }}, {{ $t('cd10') }}, {{ $t('cd11') }}, {{ $t('cd12') }},
            {{ $t('cd13') }}, {{ $t('cd14') }}
          
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap flex-center">
            <!-- <q-img style="width: 75px" src="~assets/icons/chest.png" />  -->
          <div class="q-mt-md text-center">
            {{ $t('info_chest') }}

          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlchest1"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex1') }}


          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="4" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlchest2"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex2') }}

          </div>
        </q-carousel-slide>
      </q-carousel>
    </q-dialog>
        </q-item-section>
      </q-item>

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar icon="las la-brain" color="primary" text-color="white" />
        </q-item-section>


    <q-item-section>
          <q-item-label lines="1">{{$t('home_btn_brain') }}</q-item-label>
          <q-item-label caption>{{ $t('info_cap_brain1') }} <br>{{ $t('info_cap_brain2') }}
            
          </q-item-label>
        </q-item-section>
 
        <q-item-section side>

           <q-btn  icon="chevron_right" flat size="18px"  text-color="primary" @click="popUp2">
          
        </q-btn>

  <q-dialog v-model="carousel2" full-height>
    <q-carousel
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      v-model="slide_brain"
      control-color="primary"
      arrows
      navigation
      padding
      class="bg-white shadow-1 rounded-borders"
    >
      <q-carousel-slide :name="1" class="column no-wrap flex-center">
      <div class="q-mt-md text-center text-weight-bold" style="font-size: 17px; width: 360px">
            {{ $t('info_carousel_title') }}<br>
             </div> 
        <div class="q-mt-md text-center">
      <br><br> {{ $t('tumor') }}, {{ $t('no_tumor') }} <br><br>
        </div>
      </q-carousel-slide>
      <q-carousel-slide :name="2" class="column no-wrap flex-center">
  
        <div class="q-mt-md text-center">
      {{ $t('info_brain') }}
        </div>
      </q-carousel-slide>
      <q-carousel-slide :name="3" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlbrain1"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex1') }}

          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="4" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlbrain2"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex2') }}

          </div>
        </q-carousel-slide>
    </q-carousel>
  </q-dialog>
      </q-item-section>
    </q-item>


    <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar icon="las la-allergies" color="primary" text-color="white" />
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">{{$t('home_btn_skin') }}</q-item-label>
          <q-item-label caption>  {{ $t('info_cap_skin1') }} <br>{{ $t('info_cap_skin2') }} </q-item-label>
        </q-item-section>

        <q-item-section side>

      
             <q-btn  icon="chevron_right" flat size="18px"  text-color="primary" @click="popUp3">
        
       </q-btn>

    <q-dialog v-model="carousel3" full-height>
      <q-carousel
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        v-model="slide_skin"
        control-color="primary"
        arrows
        navigation
        padding
        class="bg-white shadow-1 rounded-borders"
      >
        <q-carousel-slide :name="1" class="column no-wrap flex-center">
          <div class="q-mt-md text-center text-weight-bold" style="font-size: 17px">
          {{ $t('info_carousel_title') }}<br>
          </div> 
          <div class="q-mt-md text-center">
            {{ $t('sd1') }}, {{ $t('sd2') }}, {{ $t('sd3') }}, {{ $t('sd4') }},
              {{ $t('sd5') }}, {{ $t('sd6') }}, {{ $t('sd7') }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap flex-center">

          <div class="q-mt-md text-center">
            {{ $t('info_skin') }}

          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlskin1"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex1') }}

          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="4" class="column no-wrap flex-center">
          <div class="q-mt-md text-center">
         <q-img
      :src="urlskin2"
      spinner-color="white"
       height="610px"
        width= "350px"
    />{{ $t('info_carousel_ex2') }}

          </div>
        </q-carousel-slide>
  
      </q-carousel>
    </q-dialog>
        </q-item-section>
      </q-item>
      <q-separator spaced />
    </q-list>
  </div>

    
      
    </page-body>
  </page>

  

</template>

<script>
import { onActivated, onUpdated, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useQuasar } from 'quasar'
export default {
  name: 'info',

  setup () {
   const $q = useQuasar()
   const urlchest1 = ref()
   const urlchest2 = ref()
   const urlbrain1 = ref()
   const urlbrain2 = ref()
   const urlskin1 = ref()
   const urlskin2 = ref()
   onActivated(() => {
      urlchest1.value = '/images/infochest1_'+ $q.localStorage.getItem('language') +'.png'
      urlchest2.value = '/images/infochest2_'+ $q.localStorage.getItem('language') +'.png'
      urlbrain1.value = '/images/infobrain1_'+ $q.localStorage.getItem('language') +'.png'
      urlbrain2.value = '/images/infobrain2_'+ $q.localStorage.getItem('language') +'.png'
      urlskin1.value = '/images/infoskin1_'+ $q.localStorage.getItem('language') +'.png'
      urlskin2.value = '/images/infoskin2_'+ $q.localStorage.getItem('language') +'.png'
    })
    onUpdated(() => {
      urlchest1.value = '/images/infochest1_'+ $q.localStorage.getItem('language') +'.png'
      urlchest2.value = '/images/infochest2_'+ $q.localStorage.getItem('language') +'.png'
      urlbrain1.value = '/images/infobrain1_'+ $q.localStorage.getItem('language') +'.png'
      urlbrain2.value = '/images/infobrain2_'+ $q.localStorage.getItem('language') +'.png'
      urlskin1.value = '/images/infoskin1_'+ $q.localStorage.getItem('language') +'.png'
      urlskin2.value = '/images/infoskin2_'+ $q.localStorage.getItem('language') +'.png'
    })
   

   let carousel1 = ref (false)
   let carousel2 = ref (false)
   let carousel3 = ref (false)
   let slide_chest = ref(1)
   let slide_brain = ref(1)
   let slide_skin = ref(1)
   function popUp1 () {
     carousel1.value = true
     slide_chest.value =1
   

   }
   function popUp2 () {
 
     carousel2.value = true
     slide_brain.value =1


   }
   function popUp3 () {
  
     carousel3.value = true
     slide_skin.value =1

   }
    return {
      urlchest1,
      urlchest2,
      urlbrain1,
      urlbrain2,
      urlskin1,
      urlskin2,
    
      carousel1,
      carousel2,
      carousel3,

      slide_chest,
      slide_brain,
      slide_skin,
      
      stars: ref(3),

      slideVol: ref(39),
      slideAlarm: ref(56),
      slideVibration: ref(63),
      popUp1,
      popUp2,
      popUp3
    }
  }
}
</script>