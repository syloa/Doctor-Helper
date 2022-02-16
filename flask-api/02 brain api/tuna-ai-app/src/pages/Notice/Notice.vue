<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>{{ $t('title_notice') }}</template>
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
            <q-item-section><b>2021/11/29</b> {{ $t('notice_211129') }}</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
          <q-item
            to="/questions/answer"
            clickable
            v-ripple
          >
            <q-item-section><b>2021/11/21</b> {{ $t('notice_211121') }}</q-item-section>
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
