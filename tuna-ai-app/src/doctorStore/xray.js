import { reactive } from 'vue'

const state = reactive({
  images: [
    {
      id: 'id1',
      url: '/images/xrays/1.jpg',
      caption: '환자번호 0001',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id2',
      url: '/images/xrays/2.png',
      caption: '환자번호 0002',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id3',
      url: '/images/xrays/3.png',
      caption: '환자번호 0003',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id4',
      url: '/images/xrays/4.png',
      caption: '환자번호 0004',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id5',
      url: '/images/xrays/5.png',
      caption: '환자번호 0005',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id6',
      url: '/images/xrays/6.png',
      caption: '환자번호 0006',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id7',
      url: '/images/xrays/7.png',
      caption: '환자번호 0007',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id8',
      url: '/images/xrays/8.png',
      caption: '환자번호 0008',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id9',
      url: '/images/xrays/9.png',
      caption: '환자번호 0009',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    },
    {
      id: 'id10',
      url: '/images/xrays/10.png',
      caption: '환자번호 0010',
      date: '2021/03/01',
      age: '55',
      memo: '야옹',
      bookmarkbool: false,
      predbool: false,
      memobool: false
    }
  ],
  usePageTransition: false,
  iosBrowserSwipingBack: false
})

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