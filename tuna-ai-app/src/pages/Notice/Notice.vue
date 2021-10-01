<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>공지</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
<!-- 
        <div class="text-h5 q-mb-md"> </div> -->

        <q-list bordered separator>
          <q-item
            to="/questions/answer"
            clickable
            v-ripple
          >
            <q-item-section><b>2021/11/21</b> 1.01 버전의 업데이트 내용을 확인하세요.</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
          <q-item
            to="/questions/answer"
            clickable
            v-ripple
          >
            <q-item-section><b>2021/11/21</b> 닥터헬퍼가 출시되었습니다.</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </page-body>
  </page>
</template>

<script>
export default {
  name: 'Questions'
}
</script>
