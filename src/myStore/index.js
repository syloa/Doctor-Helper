// 네비게이션 바

import { reactive } from 'vue'

const state = reactive({
  navItems: [
    {
      root: '/home',
      to: '/home',
      icon: 'las la-home',
      label: '홈'
    },
    {
      root: '/questions',
      to: '/questions',
      icon: 'las la-question-circle',
      label: '질문'
    },
    // detect로 바꾸고 싶으면, 클릭할 때 root에 붙을 path를 변수화하여 뒤에 달아주어야 한다.
    // {
    //   root: '/xrays',
    //   to: '/xrays',
    //   icon: 'las la-image',
    //   label: 'X-Ray'
    // },
    {
      root: '/ex',
      to: '/ex',
      icon: 'las la-tty',
      label: 'ex'
    }
  ],
  images: [
    {
      id: 'id1',
      url: '/images/1.jpg',
      caption: 'Tiger',
      predict: false
    },
    {
      id: 'id2',
      url: '/images/2.jpg',
      caption: 'Man',
      predict: false
    },
    {
      id: 'id3',
      url: '/images/3.jpg',
      caption: 'Mountains',
      predict: false
    },
    {
      id: 'id4',
      url: '/images/4.jpg',
      caption: 'Road in Mountains',
      predict: false
    },
    {
      id: 'id5',
      url: '/images/5.jpg',
      caption: 'Nightime Hills',
      predict: false
    },
    {
      id: 'id6',
      url: '/images/6.jpg',
      caption: 'Cute dog',
      predict: false
    }
  ],
  usePageTransition: false,
  iosBrowserSwipingBack: false
})

  // find _ 하나 찾음 vs filter _ 여러 개 찾음 
const getters = {
  getImage(imageId) {
    return state.images.filter(image => image.id === imageId)[0]
  },

  getIndex(imageId) {
    // return state.images.map(function(d) { return d['id']}).indexOf(imageId)
    return state.images.map(image => { return image['id']}).indexOf(imageId)
  }
}

const store = {
  state,
  getters
}

export default store