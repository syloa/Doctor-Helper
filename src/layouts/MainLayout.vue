<template>
  <q-layout
    view="lHh Lpr lFf"
    :class="{ 'ios-browser-swiping-back' : store.state.iosBrowserSwipingBack }"
  >
    <!-- footer = 화면의 하단 -->
    <q-footer bordered class="bg-white text-primary">
      <!--탭 관련 참고 https://quasar.dev/vue-components/tabs -->
      <q-tabs
        active-color="primary"
        indicator-color="transparent"
        class="text-grey"
        no-caps
      >
        <q-route-tab
          v-for="navItem in store.state.navItems"
          :key="navItem.root"
          :to="navItem.to"
          :label="navItem.label"
          :icon="navItem.icon"
        />

      </q-tabs>
    </q-footer>

    <q-page-container>
      <router-view v-slot="{ Component }">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
import store from 'src/myStore'

export default {
  name: 'MainLayout',

  setup () {
    return {
      store
    }
  }
}
</script>
