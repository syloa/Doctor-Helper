<template>
  <page>
    <page-header>
      <template #buttons-left>
        <page-header-btn-back
        />
      </template>
      <template #title>설정</template>
      <template #buttons-menu>
      <page-header-btn-menu
      />
      </template>
    </page-header>
    <page-body>
      <div class="q-pa-lg">
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

   <br><div class="text-h5 q-mb-md"><b>언어 설정</b></div>

  <div class="q-pa-xs">
    <q-btn-dropdown color="primary" label="Dropdown Button" dropdown-icon="change_history">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Photos</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Videos</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Articles</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
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
      
  
      </div>
    </page-body>
  </page>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Questions',
    setup () {
    const submitResult = ref([])
    
    return {
      hex: ref('#FF00FF'),
      group: ref('op1'),
      group2: ref('op1'),
      color: ref('#f66363'),
      submitResult,

      onSubmit (evt) {
        const formData = new FormData(evt.target)
        const data = []

        for (const [ name, value ] of formData.entries()) {
          data.push({
            name,
            value
          })
        }

        submitResult.value = data
      },
      options: [
        {
          label: '라이트모드',
          value: 'op1'
        },
        {
          label: '다크모드',
          value: 'op2'
        },
      ],
      options2: [
        {
          label: '동의',
          value: 'op1'
        },
        {
          label: '미동의',
          value: 'op2'
        },
      ],
      onItemClick () {
        // console.log('Clicked on an Item')
      }
    }
  }
}
</script>
<style lang="sass" scoped>
.my-picker
  max-width: 250px
</style>
