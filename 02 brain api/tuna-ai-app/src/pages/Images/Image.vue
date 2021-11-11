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
            <p>애국가의 가사는 1900년대 초에 쓰여졌다. 작사자는 크게 윤치호라는 설과 안창호라는 설 두 가지가 있으며, 국사편찬위원회의 공식적인 입장으로는 미상이다. 작사자 윤치호 설은 윤치호가 애국가의 가사를 1907년에 써서 후에 그 자신의 이름으로 출판했다는 것이다. 한편 안창호가 썼다는 주장은 안창호가 애국가를 보급하는 데에 앞장섰다는 데에 중점을 두고 있다. 1908년에 출판된 가사집 《찬미가》에 수록된 것을 비롯한 많은 일제 강점기의 애국가 출판물은 윤치호를 작사자로 돌리고 있는 등 윤치호 설에는 증거가 많은 반면[4] 안창호 설에는 실증적인 자료가 부족하다.</p>
            <!-- <div class="q-pa-md q-gutter-sm"> -->
              <div class="fit row wrap justify-center items-start content-start">
              <!-- <q-btn style="background: #FF0080; color: white" label="Fuchsia" />
              <q-btn flat style="color: #FF0080" label="Fuchsia Flat" />
              <q-btn style="background: goldenrod; color: white" label="Goldenrod" />
              <q-btn outline style="color: goldenrod;" label="Goldenrod" /> -->
              <q-btn color="grey-4" text-color="purple" glossy unelevated icon="camera_enhance" label="Purple text" @click="ChangeValue" />
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
// mysotre의 데이터 가져옴
import store from 'src/myStore'

export default {
  name: 'Image',
  setup() {

    let image = ref()
    let idx = ref() // ref = reference. 참조하는 값을 변수로 선언
    // 내부에서만 쓰니까 ref안써도 됨. 

    onActivated(() => {  // 화면이 로드되었을 때 무조건 실행
      let route = useRoute()
      image.value = store.getters.getImage(route.params.id)   // index.js에서 만들어진 이미지함수 호출
      idx.value = store.getters.getIndex(route.params.id)
      // console.log('입력 전', store.state.images)
      // console.log(idx.value)) // ref로 만든 것엔 꼭 .value 붙어줘야함. 템플릿 윗부분에서 쓸려면 ref함수 써야
    })
// 화면에서 떠났을 때 처리
    onDeactivated(() => {
      image.value = null
    })

    function ChangeValue(){
      store.state.images[idx.value].predict = true
      console.log('입력 완료', store.state.images)

    }
    return {
      store,
      image,
      ChangeValue
    }
  }
}
</script>

