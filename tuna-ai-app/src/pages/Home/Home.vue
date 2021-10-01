<template>
  <page>
    <page-header>
      <template #title>집</template>
      <template #buttons-right>
      <page-header-btn-bookmark
        label=""
      />
      </template>
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
                <q-card-section>
                    <div>
                        <span class="text-weight-bold" style="font-size: 17px">닥터핼프</span> 
                        <span class="text-weight-light" style="font-size: 17px">&nbsp; 님</span>
                    </div>
                    <div class="text-weight-bold" style="font-size: 24px">
                        <span style="background: linear-gradient(to top, #ffc127 20%, transparent 50%)">20 건의</span>
                    </div>
                    <div class="text-weight-bold" style="font-size: 17px">의뢰가 있습니다.</div>
                    <!-- 
                    <div style="margin-top: 5px">
                        <q-btn rounded class="manage-button justify-center" color="primary" icon-right="navigate_next" >
                            관리하기
                        </q-btn>
                    </div> 
                    -->
                </q-card-section>
                <q-card-section style="margin-left: 10px">
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
                </q-card-section>                    
            </q-card-section>          
        </q-card>
    </div>
    <!-- contents -->
    <div class="text-weight-medium  text-h6" style="font-weight: 500; margin-left: 20px ;background-color: #fbfbfb;">
        <span style="color: #e4363e; width: 2px">&#124;</span> 닥터 핼프 서비스 #1
    </div>
    <div class="q-pa-md row items-start q-gutter-sm justify-between" style="margin-left: 0px">
        <q-card 
          @click="goXray"
          align="center" 
          bordered  
          flat 
          style="width: 360px; height: 135px; border-radius: 13px; "
        >
            <q-img style="width: 50px; margin-top: 18px" src="~assets/icons/service.svg" /> 
            <br>
            <br>
            <span class="text-weight-bold text-size-14">흉부 X-RAY</span>
        </q-card>
        <q-card  @click="goBrain" bordered  flat align="center" style="width: 360px; height: 135px; border-radius: 13px;">
            <q-img style="width: 50px; margin-top: 18px" src="~assets/icons/service.svg" />  
            <br>
            <br>
            <span class="text-weight-bold text-size-14">뇌종양</span>
        </q-card>
        <q-card  @click="goSkin" bordered  flat align="center" style="width: 360px; height: 135px; border-radius: 13px;">
            <q-img style="width: 50px; margin-top: 18px" src="~assets/icons/service.svg" />  
            <br>
            <br>
            <span class="text-weight-bold text-size-14">피부암</span>
        </q-card>
    </div>
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
import { ref } from 'vue'
export default {
  name: 'Home',
  setup () {
    const $router = useRouter()
    
    function goXray() {
      $router.push('/xrays')
    }

    function goSkin() {
      $router.push('/skins')
    }
    
     function goBrain() {
      $router.push('/brains')
    }

    return {
      goXray,
      goSkin,
      goBrain
    }

  }
}


</script>