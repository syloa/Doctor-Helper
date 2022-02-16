<template>
  <page>
    <page-header>
      <template #title>질문</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">

        <div class="text-h5 q-mb-md">당신이 궁굼한 것이 무엇인가요?</div>

        <q-list bordered separator>
          <q-item
            to="/questions/answer"
            clickable
            v-ripple
          >
            <q-item-section>첫번째 질문?</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
          <q-item
            to="/questions/answer"
            clickable
            v-ripple
          >
            <q-item-section>두번째 질문?</q-item-section>
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
