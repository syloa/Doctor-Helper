<template>
  <page>
    <page-header>
      <template #title>top</template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">

        <div class="text-h5 q-mb-md">test</div>

        <q-list bordered separator>
          <q-item
            to="/label/bottom"
            clickable
            v-ripple
          >
            <q-item-section>everyone is stupid</q-item-section>
            <q-item-section avatar>
              <q-icon color="primary" name="chevron_right" />
            </q-item-section>
          </q-item>
          <q-item
            to="/label/bottom2"
            clickable
            v-ripple
          >
            <q-item-section>no one is stupid</q-item-section>
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
  name: 'Top'
}
</script>
