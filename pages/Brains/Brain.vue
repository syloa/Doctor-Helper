<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="뇌 CT"
        />
      </template>
      <template #title>상세 이미지</template>
    </page-header>
    <page-body>
      <transition
        appear
        enter-active-class="animated fadeIn slower"
        leave-active-class="animated fadeOut slower"
      >
        <!-- 진단할 이미지 -->
        <div
          v-if="image"
          class="row justify-center"
        >
          <div class="text-h5 q-mb-md">{{ image.caption }}</div>
          <div class="q-mb-md">
            <q-img
              :src="image.url"
              class="no-pointer-events"
              no-transition
              no-spinner
              style="width:360px"
              >
            <div class="absolute-bottom-right">
            <q-btn
              push round dense color="white" text-color="primary"
              :icon="fullscreen ? 'fullscreen_exit' : 'fullscreen'"
              @click="maximize"
              style="width:10px"

            />
            </div>
            </q-img>
          </div>
          <div class="q-pa-lg">
            <q-btn 
              class="btn-fixed-width"
              color="primary" 
              label="진단" 
              @click="loadData" 
          />
          </div>

          <!-- 진단 결과 -->
          <div
            v-if="data"
            class="row justify-center"
          >
            <div class="text-h6 q-mb-md">진단명 : {{ data.diagnosis }} <br/>
            나이 : {{ image.age }} <br/>촬영 일자 : {{ image.date }}</div>
            <div class="q-mb-md">
            <q-img
              :src="data.img_url"
              class="no-pointer-events"
              no-transition
              no-spinner
              style="width:360px"
            >
            <div class="absolute-bottom-right">
            <q-btn
              push round dense color="white" text-color="primary"
              :icon="fullscreen ? 'fullscreen_exit' : 'fullscreen'"
              @click="maximize"
              style="width:10px"

            />
            </div>
            </q-img>
            </div>
            <div class="q-pa-md q-gutter-sm" >
            <q-editor
              v-model="editor"
              :definitions="{
                save: {
                  tip: 'Save your work',
                  icon: 'save',
                  label: 'Save',
                  handler: saveWork
                }
              }"
              :toolbar="[
                ['bold', 'italic', 'strike', 'underline'],
                ['save', '         ']
              ]"
            />
          </div>
          <div class="q-pa-md">
            <q-btn color="black" icon="save" label="결과 저장하기" @click=memoSaved />
            <q-chip
             v-model:selected="desert.Eclair" @click=bookmark color="teal" text-color="white" icon="bookmark">
              Bookmark
            </q-chip>
          </div>
          </div>
          
          
        </div>
        
        
      </transition>
    </page-body>
  </page>
</template>

<script>
import { onActivated, onDeactivated, ref } from 'vue'
import { useRoute } from 'vue-router'
import store from 'src/doctorStore/brain.js'
import { axios, api_brain } from 'boot/axios'
import { useQuasar } from 'quasar'
import { reactive, computed } from 'vue'

export default {
  name: 'Brain',
  setup() {
    // 이미지를 읽어 들여 버퍼에서 변환 처리
    var Buffer = require('buffer/').Buffer

    const $q = useQuasar() 
    const data = ref(null)
    // 이미지를 담기 위한 변수 선언
    const file = ref(null)
    let image = ref()
    let idx = ref()
    
    // 브라우저에서는 fs 모듈을 사용 불가
    // axios로 이미지 읽어 들인 후 base 64로 변환 처리
    async function getBase64(url) {
      return axios
        .get(url, {
          responseType: 'arraybuffer'
        })
        .then(response => Buffer.from(response.data, 'binary').toString('base64'))
    }

    // 이미지 담기
    // file.value = getBase64('/images/xrays/2.png')
    
    // 해당 페이지를 오픈 할 경우 활성화
    onActivated(() => {
      let route = useRoute()
      image.value = store.getters.getImage(route.params.id)
      idx.value = store.getters.getIndex(route.params.id)
    })
    // 해당 페이지를 닫을 경우 이미지 변수 null 처리
    onDeactivated(() => {
      image.value = null
      data.value = null
    })

    // 내가 추가한 부분
    function bookmark(){
      if (store.state.images[idx.value].status !== 3){
        $q.notify({
          message: '결과를 저장해주세요',
          color: 'red-5',
          textColor: 'white',
          icon: 'warning'
        })
      }
      else if (store.state.images[idx.value].bookmark === true){
        store.state.images[idx.value].bookmark = false
        console.log('북마크 off', store.state.images[idx.value])
      } else {
        store.state.images[idx.value].bookmark = true
        console.log('북마크 on', store.state.images[idx.value])
      }
    }

    function memoSaved(){
      if (store.state.images[idx.value].status !== 2){
        $q.notify({
          message: '메모를 저장해주세요',
          color: 'red-5',
          textColor: 'white',
          icon: 'warning'
        })
      }
      else {
      $q.notify({
          message: '결과를 저장했습니다.',
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done'
        })
      store.state.images[idx.value].status = 3
      console.log('메모까지 저장', store.state.images)
    }
    }
    const desert = reactive({
      Eclair: false,
    })
    
    const text = ref ('메모를 입력하세요' )
    
    function saveWork () {
        $q.notify({
          message: '메모를 저장했습니다.',
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done'
        })
        store.state.images[idx.value].memo = text.value
        store.state.images[idx.value].status = 2
        console.log('메모 저장', store.state.images)
      }

    //  이미지 확대 관련
     const fullscreen = ref (false)

     function maximize(e) {
       fullscreen.value = !fullscreen.value
       const target = e.target.parentNode.parentNode.parentNode

        $q.fullscreen.maximize(target)
          .then(() => {
          })
          .catch((err) => {
            alert(err)
          })
      }
    
    function getFileName(fileUrl) {
      // URL을 가져와서 '/' 기준으로 배열 분리
      var filePathSplit = fileUrl.split('/');
      // 배열 분리 후 마지막 배열에서 다시 '.' 기준으로 분리
      var fileNameSplit = filePathSplit[filePathSplit.length -1].split('.')
      // 해당 파일의 첫번째 배열값 반환
      var fileName = fileNameSplit[0]

      return fileName
    }

    // 데이터 불러들여 처리
    async function loadData () {
      // 이미지 담기
      // const file = await getBase64('/images/xrays/1.jpg')
      // url로 접근해서 처리하는 방식이라 파일명을 함수로 못가져옴
      // 잘라서 가져오는 함수 구현
      store.state.images[idx.value].status = 1
      console.log('진단', store.state.images)
      const fileName = getFileName(image.value.url)
      const file = await getBase64(image.value.url)
      const base64 = 'data:image/jpg;base64,' + file;
      const blob = await fetch(base64).then(res => res.blob())

      // console.log('base64 ======> ', base64)
      // console.log('blob ======> ', blob)
      const formData = new FormData() 
      // form에 파일 정보 담기
      // 이미지 파일과 파일명
      formData.append('file', blob); 
      formData.append('fileName', fileName);

      // rest api로 예측 요청 넘기기
      api_brain.post('/predict', formData , { 
        headers: {
          'Content-Type': 'multipart/form-data'
        }
       })
        .then((response) => {
          // rest-api로 보낸 이미지 예측 결과값 받아오기
          console.log('response.data : ', response.data)
          data.value = response.data
        })
        .catch((e) => {
          // 처리 오류의 경우 화면에 notice
          $q.notify({
            color: 'negative',
            position: 'top',
            message: '진단이 실패하였습니다.',
            icon: 'report_problem'
          })
        })
    }
    

    return {
      store,
      image,
      data,
      loadData,
      memoSaved,
      bookmark,
      desert,
      editor: text,
      saveWork,
      fullscreen,
      maximize,
    }
  }
}
</script>
<style lang="sass" scoped>
.btn-fixed-width
  width: 200px
</style>