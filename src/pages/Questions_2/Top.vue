<template>
  <page>
    <page-header>
      <template #title>변경</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">

        <div class="text-h5 q-mb-md">실험</div>

        <q-list bordered separator>
          <q-item
            to="/top/bottom"
            clickable
            v-ripple
          >
            <q-item-section>첫번째 실험?</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
          <q-item
            to="/top/bottom"
            clickable
            v-ripple
          >
            <q-item-section>두번째 실험?</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
            
          </q-item>
          <q-item
            to="/top/bottom"
            clickable
            v-ripple
          >
            <q-item-section>세번째 실험?</q-item-section>
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
