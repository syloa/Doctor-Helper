<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>{{ $t('title_setting') }}</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>

       <page-body>      
          <q-list bordered padding>
            <q-item-label header>{{ $t('setting_subtitle_user') }}</q-item-label>
          
            <q-item clickable v-ripple>
                <q-item-section>
                <q-item-label>{{ $t('setting_subtitle_language') }}</q-item-label>
                <q-item-label>
                    <q-select
                        v-model="locale"
                        :options="localeOptions"
                        dense
                        emit-value
                        map-options
                        options-dense
                        style="min-width: 150px"
                    />
                </q-item-label>
                </q-item-section>
            </q-item>

            <q-separator spaced />
            <q-item-label header>{{ $t('setting_subtitle_color') }}</q-item-label>

            <!-- <q-item tag="label" v-ripple>
                <q-item-section side top>
                    <q-checkbox v-model="darkMode" @click="checkDarkMode" />
                </q-item-section>
                <q-item-section>
                <q-item-label>다크모드</q-item-label>
                <q-item-label caption>
                    다크모드 설정 
                </q-item-label>
                </q-item-section>`
            </q-item> -->

            <q-item tag="label">
                <q-item-section>
                    <div class="row justify-center">
                        <q-color 
                            v-model="colorPrimaryHex" 
                            no-header 
                            @click="setColor" 
                            style="width: 250px"
                        />
                    </div>
                </q-item-section>
            </q-item>
            <div class="q-gutter-md row justify-center">
            <q-btn color="primary" icon="settings_backup_restore" :label="$t('setting_btn_reset')" @click="reset" />
          </div>

            <q-separator spaced />
            <q-item-label header>{{ $t('setting_subtitle_others') }}</q-item-label>

            <q-item tag="label" v-ripple>
                <q-item-section>
                <q-item-label>{{ $t('setting_others_battery') }}</q-item-label>
                <q-item-label caption>{{ $t('setting_others_battery_detail') }}</q-item-label>
                </q-item-section>
                <q-item-section side >
                <q-toggle color="primary" v-model="notif1" val="battery" />
                </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
                <q-item-section>
                <q-item-label>{{ $t('setting_others_email') }}</q-item-label>
                <q-item-label caption>{{ $t('setting_others_email_detail') }}</q-item-label>
                </q-item-section>
                <q-item-section side top>
                <q-toggle color="primary" v-model="notif2" val="friend" />
                </q-item-section>
            </q-item>

        </q-list>
        <!-- <q-list bordered padding>
            <q-item-label header>{{ $t('setting_subtitle_user') }}</q-item-label>

            <q-item clickable v-ripple>
                <q-item-section>
                <q-item-label>Content filtering</q-item-label>
                <q-item-label caption>
                    Set the content filtering level to restrict
                    apps that can be downloaded
                </q-item-label>
                </q-item-section>
            </q-item>
        </q-list>

            <q-item clickable v-ripple>
                <q-item-section>
                <q-item-label>Password</q-item-label>
                <q-item-label caption>
                    Require password for purchase or use
                    password to restrict purchase
                </q-item-label>
                </q-item-section>
            </q-item>
            
            <q-item-label header>{{ $t('setting_subtitle_language') }}</q-item-label>
            <q-item clickable v-ripple>
                <q-item-section>
                <q-item-label>{{ $t('setting_subtitle_language') }}</q-item-label>
                <q-item-label>
                    <q-select
                        v-model="locale"
                        :options="localeOptions"
                        dense
                        emit-value
                        map-options
                        options-dense
                        style="min-width: 150px"
                    />
                </q-item-label>
                </q-item-section>
            </q-item>

            <q-separator spaced /> -->
            <!-- <q-item-label header>일반</q-item-label>

            <q-item tag="label" v-ripple>
                <q-item-section side top>
                    <q-checkbox v-model="darkMode" @click="checkDarkMode" />
                </q-item-section>

                <q-item-section>
                <q-item-label>다크모드</q-item-label>
                <q-item-label caption>
                    다크모드 설정 
                </q-item-label>
                </q-item-section>
            </q-item> -->
                <!-- <q-item-label header>{{ $t('setting_subtitle_color') }}</q-item-label>
            <q-item tag="label">
                <q-item-section>
                    <div class="row justify-center">
                        <q-color 
                            v-model="colorPrimaryHex" 
                            no-header 
                            @click="setColor" 
                            style="width: 250px"
                        />
                    </div>
                </q-item-section>
            </q-item> -->

            <!-- <q-item tag="label" v-ripple>
                <q-item-section side top>
                <q-checkbox v-model="check3" />
                </q-item-section>

                <q-item-section>
                <q-item-label>Auto-add widgets</q-item-label>
                <q-item-label caption>
                    Automatically add home screen widgets
                </q-item-label>
                </q-item-section>
            </q-item> -->
<!-- 
            <q-separator spaced />
            <q-item-label header>Notifications</q-item-label>

            <q-item tag="label" v-ripple>
                <q-item-section>
                <q-item-label>Battery too low</q-item-label>
                </q-item-section>
                <q-item-section side >
                <q-toggle color="blue" v-model="notif1" val="battery" />
                </q-item-section>
            </q-item> -->
<!-- 
            <q-item tag="label" v-ripple>
                <q-item-section>
                <q-item-label>Friend request</q-item-label>
                <q-item-label caption>Allow notification</q-item-label>
                </q-item-section>
                <q-item-section side top>
                <q-toggle color="green" v-model="notif2" val="friend" />
                </q-item-section>
            </q-item> -->
<!-- 
            <q-item tag="label" v-ripple>
                <q-item-section>
                <q-item-label>Picture uploaded</q-item-label>
                <q-item-label caption>Allow notification when uploading images</q-item-label>
                </q-item-section>
                <q-item-section side top>
                <q-toggle color="red" v-model="notif3" val="picture" />
                </q-item-section>
            </q-item>
        </q-list> -->


      <!-- <div class="q-pa-lg">
           <div class="text-h5 q-mb-md"><b>화면 설정</b></div>
      
        <div class="q-pa-xs">
          <q-option-group
            v-model="group"
            :options="options"
            color="primary"
            inline
            dense
          />
        </div>
<br>
          <div class="text-h5 q-mb-md"><b>사용자 지정 테마</b></div>

         <div class="q-pa-xs">
    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-color
        name="accent_color"
        v-model="color"
        style="width: 200px; max-width: 100%;"
      />

      <div>
        <q-btn label="SAVE" type="submit" color="primary"/>
      </div>
    </q-form>

    <q-card flat bordered class="q-mt-md bg-grey-2" v-if="submitResult.length > 0">
      <q-card-section>Submitted form contains the following formData (key = value):</q-card-section>
      <q-separator />
      <q-card-section class="row q-gutter-sm items-center">
        <div
          v-for="(item, index) in submitResult"
          :key="index"
          class="q-px-sm q-py-xs bg-grey-8 text-white rounded-borders text-center text-no-wrap"
        >{{ item.name }} = {{ item.value }}</div>
      </q-card-section>
    </q-card>
  </div>
   <br><div class="text-h5 q-mb-md"><b>이메일 수신 동의</b></div>

        <div class="q-pa-xs">
          <q-option-group
            v-model="group2"
            :options="options2"
            color="primary"
            inline
            dense
          />
        </div>
      </div> -->



    </page-body>
  </page>
</template>

<script>
import { ref, onUpdated, onActivated, onDeactivated, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useQuasar, getCssVar, setCssVar  } from 'quasar'

export default {
  name: 'Questions',
    setup () {
    const submitResult = ref([])

    const $q = useQuasar()
    const { locale } = useI18n({ useScope: 'global' })
    const localeOptions = [
        { value: 'en-US', label: 'English' },
        { value: 'ko', label: '한국어' },
        { value: 'eo', label: 'Esperanto'}
    ]
    
    const darkMode = ref(null)
    // const colorPrimary = ref(null)
    const colorPrimaryHex = ref(getCssVar('primary'))
    darkMode.value = $q.localStorage.getItem(darkMode) ? false : true
    // colorPrimary.value = getCssVar('primary')
    // console.log('darkMode.value', darkMode.value)
    // console.log('colorPrimary.value', colorPrimary.value)
    // console.log('colorPrimaryHex.value', colorPrimaryHex.value)
    const checkDarkMode = (() => {
        // console.log('log Dark Mode', darkMode.value)
        $q.localStorage.set('darkMode', darkMode.value)
        $q.dark.set(darkMode.value)
    })
    const setColor = (() => {
        setCssVar('primary', colorPrimaryHex.value)
        $q.localStorage.set('primary', colorPrimaryHex.value)
    })
    const reset = (() => {
        setCssVar('primary', '#009688')
        $q.localStorage.set('primary', '#009688')
        colorPrimaryHex.value = '#009688'
        locale.value = 'ko'
        $q.localStorage.set('language', 'ko')
    })
    onUpdated(() => {
    $q.localStorage.set('language', locale.value)
})
    onDeactivated(() => {
    $q.localStorage.set('language', locale.value)
})
    watch(locale,() => {
    $q.localStorage.set('language', locale.value)
    // console.log(locale.value)    
    })

    return {
      // hex: ref('#FF00FF'),
      // group: ref('op1'),
      // group2: ref('op1'),
      // color: ref('#f66363'),
      // submitResult,

      // onSubmit (evt) {
      //   const formData = new FormData(evt.target)
      //   const data = []

      //   for (const [ name, value ] of formData.entries()) {
      //     data.push({
      //       name,
      //       value
      //     })
      //   }

      //   submitResult.value = data
      // },
      // options: [
      //   {
      //     label: '라이트모드',
      //     value: 'op1'
      //   },
      //   {
      //     label: '다크모드',
      //     value: 'op2'
      //   },
      // ],
      // options2: [
      //   {
      //     label: '동의',
      //     value: 'op1'
      //   },
      //   {
      //     label: '미동의',
      //     value: 'op2'
      //   },
      // ],
      // onItemClick () {
      //   // console.log('Clicked on an Item')
      // },
      
      darkMode,
      locale,
      localeOptions: [
          { value: 'en-US', label: 'English' },
          { value: 'ko', label: '한국어' },
          { value: 'eo', label: 'Esperanto'}
      ],
      check2: ref(false),
      check3: ref(false),
      notif1: ref(true),
      notif2: ref(true),
      notif3: ref(false),
      checkDarkMode,
      colorPrimaryHex,
      setColor,
      reset    
      }
  }
}
</script>
<style lang="sass" scoped>
.my-picker
  max-width: 250px
</style>
