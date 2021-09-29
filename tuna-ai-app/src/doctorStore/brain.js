import { reactive } from 'vue'

const state = reactive({
  images: [
    {
      id: 'id1',
      url: '/images/brains/1.jpg',
      caption: '환자번호 0001',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id2',
      url: '/images/brains/2.jpg',
      caption: '환자번호 0002',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id3',
      url: '/images/brains/3.jpg',
      caption: '환자번호 0003',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id4',
      url: '/images/brains/4.jpg',
      caption: '환자번호 0004',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id5',
      url: '/images/brains/5.jpg',
      caption: '환자번호 0005',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id6',
      url: '/images/brains/6.jpg',
      caption: '환자번호 0006',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id7',
      url: '/images/brains/7.jpg',
      caption: '환자번호 0007',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id8',
      url: '/images/brains/8.jpg',
      caption: '환자번호 0008',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id9',
      url: '/images/brains/9.jpg',
      caption: '환자번호 0009',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
    },
    {
      id: 'id10',
      url: '/images/brains/10.jpg',
      caption: '환자번호 0010',
      date: '2021/03/01',
      age: '55',
      memo: '야옹'
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