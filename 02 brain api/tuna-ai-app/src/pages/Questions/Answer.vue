<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
          label="질문"
        />
      </template>
      <template #title>Answer</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
        <div class="text-h5 q-mb-md">무엇이든 물어보세요</div>

        <p v-for="i in 20" :key="i">애국가의 가사는 1900년대 초에 쓰여졌다. 작사자는 크게 윤치호라는 설과 안창호라는 설 두 가지가 있으며, 국사편찬위원회의 공식적인 입장으로는 미상이다. 작사자 윤치호 설은 윤치호가 애국가의 가사를 1907년에 써서 후에 그 자신의 이름으로 출판했다는 것이다. 한편 안창호가 썼다는 주장은 안창호가 애국가를 보급하는 데에 앞장섰다는 데에 중점을 두고 있다. 1908년에 출판된 가사집 《찬미가》에 수록된 것을 비롯한 많은 일제 강점기의 애국가 출판물은 윤치호를 작사자로 돌리고 있는 등 윤치호 설에는 증거가 많은 반면[4] 안창호 설에는 실증적인 자료가 부족하다.</p>
      </div>
    </page-body>
  </page>
</template>

<script>
export default {
  name: 'Answer'
}
</script>
