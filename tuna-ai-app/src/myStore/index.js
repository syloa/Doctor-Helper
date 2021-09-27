import { reactive } from 'vue'
// state 밑에 images, 그 밑에 배열
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
    // {
    //   root: '/xrays',
    //   to: '/xrays',
    //   icon: 'las la-image',
    //   label: 'X-Ray'
    // },
    // {
    //   root: '/skins',
    //   to: '/skins',
    //   icon: 'las la-image',
    //   label: '피부암'
    // }
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

// 이미지를 가져오는 것.
// setter 만들어서 변경하거나 저장하기도 가능.
// 실제 이미지 id넣었을 때 이 이미지 id가 배열에서 순서가 몇번째인지를
// 가져오는 함수를 만들것.

// const getters = {
//   getImage(imageId) {
//     return state.images.filter(image => image.id === imageId)[0]
//   }
// }

const getters = {
  getImage(imageId) {
    return state.images.filter(image => image.id === imageId)[0]
  },

  getIndex(imageId) {
    // return state.images.map(function(d) { return d['id']}).indexOf(imageId)
    return state.images.map(image => { return image['id']}).indexOf(imageId)
  }
}


// find 함수 = 유일한 하나, filter = 같은 것 여러개 찾음.
const store = {
  state,
  getters
}

export default store