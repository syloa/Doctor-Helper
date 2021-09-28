<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="갤러리"
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
        <div
          v-if="image"
        >
          <q-img
            :src="image.url"
            class="no-pointer-events"
            no-transition
            no-spinner
          />
          <div class="q-pa-lg">
            <div class="text-h5 q-mb-md">{{ image.caption }}</div>
            <p>애국가의 가사는 1900년대 초에 쓰여졌다. </p>
          </div>
            <!-- 중앙에 배치 - (Flex playground) -->
            <div class='fit row wrap justify-center items-start content-start'>
            <q-btn color="black" label="Black" @click=changeValue />
            
            </div>
        </div>
      </transition>
    </page-body>
  </page>
</template>

<script>
import { onActivated, onDeactivated, ref } from 'vue'
import { useRoute } from 'vue-router'
// mystore의 데이터 가져옴
import store from 'src/myStore'

export default {
  name: 'Image',
  setup() {

    let image = ref()

    // 빈 값 만들어놓기, 템플릿에서 사용하려면 ref() 필요
    let idx = ref()

    // 화면이 로드 되었을 때 무조건 실행
    onActivated(() => {
      let route = useRoute()
      image.value = store.getters.getImage(route.params.id)
      idx.value = store.getters.getIndex(route.params.id)
      // console.log('버튼 누르기 전', store.state.images)
      // console.log(idx.value)
    })

    // 화면에서 떠났을 때 처리
    onDeactivated(() => {
      image.value = null
    })

    function changeValue(){
      store.state.images[idx.value].predict = true
      console.log('버튼 누름', store.state.images)
    }
    return {
      store,
      image,
      changeValue,
  }
}
}
</script>
