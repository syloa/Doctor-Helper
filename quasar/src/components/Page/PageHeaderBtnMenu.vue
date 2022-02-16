<template>
  <q-btn 
  flat 
  @click="drawer = !drawer" 
  round 
  color="primary"
  dense 
  rounded
  no-caps
  icon="menu"/>

      <q-drawer
        side="right"
        v-model="drawer"
        show-if-above
        :width="200"
        :breakpoint="500"
        bordered
        class="bg-grey-3"
      >
        <q-scroll-area class="fit">
          <q-list>

            <template v-for="(menuItem, index) in menuList" :key="index">
                           
              <q-item clickable
              :active="menuItem.label === 'Outbox'" 
              v-ripple
              @click="gothere(index)">
                <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  {{ $t(menuItem.label) }}
                </q-item-section>
              </q-item>
              <q-separator :key="'sep' + index"  v-if="menuItem.separator" />
            </template>

          </q-list>
        </q-scroll-area>
      </q-drawer>



</template>

// import할때는 router로 보내야함
<script>
import { useRouter } from 'vue-router'
import { ref } from 'vue'

export default {
  name: 'PageHeaderBtnMenu',
  setup() {
    const $router = useRouter()

    function gothere(index){
      if (index===0) {
        $router.push('/home')
      }
      else if (index===1) {
        $router.push('/xrays')
      }
      else if (index===2) {
        $router.push('/brains')
      }
      else if (index===3) {
        $router.push('/skins')
      }
      else if (index===4) {
        $router.push('/settings')
      }
      else if (index===5) {
        $router.push('/notice')
      }
      else if (index===6) {
        $router.push('/bookmarks')
      }
      else if (index===7) {
        $router.push('/info')
      }
    }

    const menuList = [
      {
        icon: 'home',
        label: 'menu_home',
        separator: true,
      },
      {
        icon: 'las la-x-ray',
        label: 'menu_chest',
        separator: false
      },
      {
        icon: 'las la-brain',
        label: 'menu_brain',
        separator: false
      },
      {
        icon: 'las la-allergies',
        label: 'menu_skin',
        separator: true
      },
      {
        icon: 'settings',
        label: 'menu_setting',
        separator: false
      },
      {
        icon: 'feedback',
        label: 'menu_notice',
        separator: false
      },
      {
        icon: 'star',
        iconColor: 'primary',
        label: 'menu_bookmark',
        separator: false
      },
      {
        icon: 'help',
        iconColor: 'primary',
        label: 'menu_help',
        separator: false
      }
    ]

    return {
      drawer: ref(false),
      menuList,
      gothere
    }
  }
}
</script>