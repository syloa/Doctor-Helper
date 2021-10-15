<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>흉부 질환 진단</template>
      <template #buttons-right>
      <page-header-btn-bookmark
      />
      </template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
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
          <q-img
            :src="image.url"
            class="no-pointer-events"
            no-transition
            no-spinner
            style="width:360px"
          />
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
            <div class="text-h5 q-mb-md">진단명 : {{ data.name }} ( {{ data.rate }})<br> 촬영일자 : {{image.date}}
            <br>나이 : {{image.age}}</div>
            <q-img
              :src="data.img_url"
              class="no-pointer-events"
              no-transition
              no-spinner
              style="width:360px"
            />
                        <div class="q-pa-md q-gutter-sm" >
            <q-editor
              v-model="editor"
              style="width:380px; height:220px"
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
                ['save']
              ]"
            />
          </div>
          <div class="q-pr-md">
            <q-btn color="primary" icon="mail" label="의견 보내기" @click="sendEmail" />
            <q-btn color="primary" icon="restart_alt" label="진단 리셋" @click="DBs.resetDectection('chest', imageId)" />
          </div>
          </div>
          <div
            v-else-if="image.detect"
            class="row justify-center"
          >
            <div class="text-h6 q-mb-md">진단명 : {{ image.result }} <br/>
            나이 : {{ image.age }} <br/>촬영일 : {{ image.date }}</div>
            <div 
            class="q-mb-md">
            <q-img
              v-if="image.detected_image"
              :src="image.detected_image"
              no-transition
              no-spinner
              style="width:380px"
            >
            </q-img>
            </div>
            <div class="q-pa-md q-gutter-sm" >
            <q-editor
              v-model="editor"
              style="width:380px; height:220px"
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
                ['save']
              ]"
            />
          </div>
          <div class="q-pr-md">
            <q-btn color="primary" icon="mail" label="의견 보내기" @click="sendEmail" />
            <q-btn color="primary" icon="restart_alt" label="진단 리셋" @click="DBs.resetDectection('chest', imageId)" />
          </div>



          </div>    
        </div>
        
        
      </transition>
    </page-body>
  </page>
</template>

<script>
import { onActivated, onDeactivated, onUpdated, ref } from 'vue'
import { useRoute } from 'vue-router'
import storeXray from 'src/doctorStore/xray.js'
import { axios, api } from 'boot/axios'
import { useQuasar } from 'quasar'
import PageHeaderBtnBookmark from 'src/components/Page/PageHeaderBtnBookmark.vue'
import DBs from 'src/doctorStore/MongoDB.js'

export default {
  name: 'Chest',
  setup() {
    // 이미지를 읽어 들여 버퍼에서 변환 처리
    var Buffer = require('buffer/').Buffer

    const $q = useQuasar() 
    const data = ref(null)
    // 이미지를 담기 위한 변수 선언
    const file = ref(null)
    let image = ref()
    let idx = ref()
    let text = ref('메모를 작성해 주세요.')
    let detect = ref(false)
    let bookmarks = ref(false)
    let imageId = ref()
    let route = useRoute()
    let imageDialog = ref(false)
    let imageUrl = ref(null)
    const imagePopup = (imgUrl) => {
            imageUrl.value = imgUrl
            imageDialog.value = true
            console.log("imgUrl")
    }


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
      getXray()
      // let route = useRoute()
      // image.value = storeXray.getters.getImage(route.params.id)
      // idx.value = storeXray.getters.getIndex(route.params.id)      
    })

    onUpdated(() => {
      getXray()
    })
    // 해당 페이지를 닫을 경우 이미지 변수 null 처리
    onDeactivated(() => {
      image.value = null
      data.value = null
      bookmarks.value = null
      imageId.value = null
      detect.value = false
      text.value = '메모를 작성해 주세요.'
    })

    
    function getFileName(fileUrl) {
      // URL을 가져와서 '/' 기준으로 배열 분리
      var filePathSplit = fileUrl.split('/');
      // 배열 분리 후 마지막 배열에서 다시 '.' 기준으로 분리
      var fileNameSplit = filePathSplit[filePathSplit.length -1].split('.')
      // 해당 파일의 첫번째 배열값 반환
      var fileName = fileNameSplit[0]

      return fileName
    }

    async function getXray() {
     image.value = await DBs.getImage('chest', route.params.id)
     if ( typeof(image.value) != "undefined") {
     imageId.value = image.value["_id"]
     bookmarks.value = image.value["bookmark"]
     detect.value = image.value["detect"]
     text.value = image.value["memo"]
     console.log('hi', image.value, imageId.value, bookmarks.value, detect.value, text.value)}
    }

    async function saveWork () {
      $q.notify({
        message: 'Saved your text to local storage',
        color: 'green-4',
        textColor: 'white',
        icon: 'cloud_done'
      })
      await DBs.saveMemo('chest', imageId.value, text)
      // storeXray.state.images[idx.value].memo = editor.value
      // console.log('메모 저장', storeXray.state.images)
    }

  
    function init() {
      console.log('init', idx.value)
    }

    async function bookmark(){
      bookmarks.value = !bookmarks.value
      await DBs.saveBookmark('chest', imageId.value, bookmarks.value)
    }

    function sendEmail(){
      $q.notify({
          message: '결과를 저장했습니다.',
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done'
        })
      console.log('의견 보내기', storeBrain.state.images)
    }

    // 데이터 불러들여 처리
    async function loadData () {
      // 이미지 담기
      // const file = await getBase64('/images/xrays/1.jpg')
      // url로 접근해서 처리하는 방식이라 파일명을 함수로 못가져옴
      // 잘라서 가져오는 함수 구현
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

      $q.loading.show({
        delay: 400 // ms
      })

      // rest api로 예측 요청 넘기기
      api.post('/predict', formData , { 
        headers: {
          'Content-Type': 'multipart/form-data'
        }
       })
        .then((response) => {
          // rest-api로 보낸 이미지 예측 결과값 받아오기
          console.log('response.data : ', response.data)
          data.value = response.data
          DBs.saveDectection('chest', imageId.value, data.value.diagnosis, data.value.img_url)
          $q.loading.hide()
        })
        .catch((e) => {
          // 처리 오류의 경우 화면에 notice
          $q.notify({
            color: 'negative',
            position: 'top',
            message: 'x-ray 예측이 실패하였습니다.',
            icon: 'report_problem'
          })
          $q.loading.hide()
        })
    }
  

    return {
      storeXray,
      image,
      data,
      loadData,
      editor: text,
      saveWork,
      bookmark,
      bookmarks,
      imagePopup,
      imageDialog,
      imageUrl,
      DBs,
      imageId,
      sendEmail
    }
  }
}
</script>
<style lang="sass" scoped>
.btn-fixed-width
  width: 200px
</style>