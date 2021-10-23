<template>
  <page>
    <page-header>
      <template #title>{{ $t('title_home') }}</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>
    <page-body>
      <div class="q-pa-xs q-gutter-md row items-start " style="background-color: #fbfbfb;">
        <!-- 상단 -->
        <q-card class="top-card " flat style="margin-left: 30px" >
            <q-card-section horizontal>
              <q-card-section horizontal>
                <q-card-section>
                <q-img
              :src='profile'
              class="no-pointer-events"
              no-transition
              no-spinner
              style="width:190px; height:190px; margin-left: 10px; border-radius: 10px"
              />
              </q-card-section>   
                <q-card-section>
                    <div>
                        <span class="text-weight-bold" style="font-size: 17px">Dr.&nbsp; {{ $t('home_username') }},</span> 
                        <!-- <span class="text-weight-light" style="font-size: 17px">&nbsp; 님</span> -->
                    </div>
                    <div class="text-weight-bold" style="font-size: 24px">
                        <span style="background: linear-gradient(to top, #80CBC4 20%, transparent 50%)">
                          {{num_chest + num_brain + num_skin}} {{ $t('home_main1') }}</span>
                    </div>
                    <div class="text-weight-bold" style="font-size: 17px">{{ $t('home_main2') }}</div>
                    <!-- 
                    <div style="margin-top: 5px">
                        <q-btn rounded class="manage-button justify-center" color="primary" icon-right="navigate_next" >
                            관리하기
                        </q-btn>
                    </div> 
                    -->
                </q-card-section>
                <!-- <q-card-section style="margin-left: 10px">
                    <q-list>
                      <q-item clickable v-ripple>
                        <q-item-section avatar>
                          <q-icon color="primary" name="contacts" />
                        </q-item-section>

                        <q-item-section>흉부 X-Ray 10건</q-item-section>
                      </q-item>

                      <q-item clickable v-ripple>
                        <q-item-section avatar>
                          <q-icon color="primary" name="person_search" />
                        </q-item-section>

                        <q-item-section>뇌종양 10건</q-item-section>
                      </q-item>
                    </q-list>
                </q-card-section>                     -->
            </q-card-section> 
            </q-card-section>           
        </q-card>
    </div>
    <!-- contents -->
    <div class="text-weight-medium  text-h6" style="font-weight: 500; margin-left: 20px ;background-color: #fbfbfb;">
        <span style="color: #e4363e; width: 2px">&#124;</span> {{ $t('home_service') }}
    </div>
    <div class="q-pa-md row items-start q-gutter-sm justify-between" style="margin-left: 0px">
        <q-card 
          class="my-card" 
          @click="goXray"
          align="center" 
          bordered  
          flat 
          style="min-width: 345px; height: 115px; border-radius: 13px; "
        >
        <q-card-section horizontal>
          <q-card-section>
            <q-img style="width: 75px; " src="~assets/icons/chest.png" /> 
            <br>
            
            <span class="flex-center row text-weight-bold text-size-16">{{ $t('home_subtitle_chest') }}</span>
            </q-card-section>
            <q-card-section vertical>
            <q-card-section>  
            <span 
            class="text-weight-medium text-h6"
            style="margin-top: 30px; margin-left: 15px width:140px; height:25px">{{ $t('home_btn_chest') }}</span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"><br>{{ $t('home_btn_waiting') }}: {{ num_chest }}
            </span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"> <br>{{ $t('home_btn_completed') }}: {{num_chest_done}}</span>
          </q-card-section>
        </q-card-section>
        </q-card-section>
        </q-card>

        <q-card
          class="my-card" 
          @click="goBrain"
          align="center" 
          bordered  
          flat 
          style="width: 345px; height: 115px; border-radius: 13px; "
        >   <q-card-section horizontal>
          <q-card-section>
            <q-img style="width: 75px" src="~assets/icons/brain.png" /> 
            <br>
            <span 
            class="flex-center row text-weight-bold text-size-16">{{ $t('home_subtitle_brain') }}</span>
            </q-card-section>
            <q-card-section vertical>
            <q-card-section>  
            <span 
            class="text-weight-medium text-h6"
            style="margin-top: 30px; margin-left: 15px width:150px; height:25px">{{ $t('home_btn_brain') }}</span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"><br>{{ $t('home_btn_waiting') }}: {{ num_brain }}
            </span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"> <br>{{ $t('home_btn_completed') }}: {{num_brain_done}}</span>
          </q-card-section>
        </q-card-section>
        </q-card-section>
        </q-card>

        <q-card
          class="my-card" 
          @click="goSkin"
          align="center" 
          bordered  
          flat 
          style="width: 345px; height: 115px; border-radius: 13px; "
        >   <q-card-section horizontal>
          <q-card-section>
            <q-img style="width: 75px" src="~assets/icons/skin.png" /> 
            <br>
            <span 
            class="flex-center row text-weight-bold text-size-16">{{ $t('home_subtitle_skin') }}</span>
            </q-card-section>
            <q-card-section vertical>
            <q-card-section>  
            <span 
            class="text-weight-medium text-h6"
            style="margin-top: 30px; margin-left: 15px width:150px; height:25px">{{ $t('home_btn_skin') }}</span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"> <br>{{ $t('home_btn_waiting') }}: {{num_skin}}</span>
            <span 
            class="text-weight-medium text-size-16"
            style="margin-left: 20px width:150px; height:25px"> <br>{{ $t('home_btn_completed') }}: {{num_skin_done}}</span>
          </q-card-section>
        </q-card-section>
        </q-card-section>
        </q-card>
    </div>

<!-- 
    <div class="q-pa-md row items-start q-gutter-sm justify-between" style="margin-left: 0px">
        <q-card @click="goXray" align="center" bordered flat style="width: 345px; height: 115px; border-radius: 13px; " >
            <q-img style="width: 75px; margin-top: 18px" src="~assets/icons/chest.png" /> 
            <br>
            <br>
            <span class="text-weight-bold text-size-14">흉부 X-RAY</span>
        </q-card>
        <q-card  @click="goBrain" bordered  flat align="center" style="width: 360px; height: 135px; border-radius: 13px;">
            <q-img style="width: 50px; margin-top: 18px" src="~assets/icons/brain.png" />  
            <br>
            <br>
            <span class="text-weight-bold text-size-14">뇌종양</span>
        </q-card>
        <q-card  @click="goSkin" bordered  flat align="center" style="width: 360px; height: 135px; border-radius: 13px;">
            <q-img style="width: 50px; margin-top: 18px" src="~assets/icons/skin.png" />  
            <br>
            <br>
            <span class="text-weight-bold text-size-14">피부암</span>
        </q-card>
    </div> -->
<!-- 
    <div class="q-pa-lg">

        <div class="text-h5 q-mb-md">Tuna-AI 앱!!</div>

        <q-btn
          to="/home/child"
          label="자식 페이지로 이동"
          color="primary"
          class="full-width q-mb-md"
          rounded
          unelevated
          no-caps
        />

        <q-btn
          to="/questions/answer"
          label="질문 페이지로 이동"
          color="primary"
          class="full-width q-mb-md"
          rounded
          unelevated
          no-caps
        />
       
      </div>
       -->
    </page-body>
  </page>
</template>

<script>
// Composition API variant
import { useRouter } from 'vue-router'
import { onActivated, onDeactivated, ref, reactive, onUpdated } from 'vue'
import DBs from 'src/doctorStore/MongoDB.js'
export default {
  name: 'Home',
  setup () {
    const $router = useRouter()
    const profile = "images/profile/profile.png"
    var chestList = ref([])
    var brainList = ref([])
    var skinList = ref([])
    var num_chest = ref()
    var num_brain = ref()
    var num_skin = ref()
    var num_chest_done = ref()
    var num_brain_done = ref()
    var num_skin_done = ref()
    
    function goXray() {
      $router.push('/xrays')
    }

    function goSkin() {
      $router.push('/skins')
    }
    
     function goBrain() {
      $router.push('/brains')
    }

    function count(list, bool) {
      var cnt = 0
      for (const obj in list.value) {
        if (list.value[obj]["detect"] === bool) {
          cnt ++
        }
      }
      return cnt
    }

    async function getNum() {
      try{
        chestList.value =  await DBs.getList('chest',) 
        brainList.value =  await DBs.getList('brain') 
        skinList.value =  await DBs.getList('skin') 
        num_chest.value = await count(chestList, false)
        num_brain.value = await count(brainList, false)
        num_skin.value = await count(skinList, false)
        num_chest_done.value = await count(chestList, true)
        num_brain_done.value = await count(brainList, true)
        num_skin_done.value = await count(skinList, true)
        // console.log(num)
        // console.log(num.reduce((a, b) => a + b))
      } catch (e) {
        console.log('error', e)
      }    
    }

    onActivated(() => {
      getNum()
      console.log(num_chest)
    })
    onUpdated(() => {
      getNum()
    })
    onDeactivated(() => {
    })


    return {
      goXray,
      goSkin,
      goBrain,
      profile,
      getNum,
      num_chest,
      num_brain,
      num_skin,
      num_chest_done,
      num_brain_done,
      num_skin_done
    }

  }
}


</script>