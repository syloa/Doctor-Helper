import { reactive } from 'vue'

const state = reactive({
  images: [
    // status : 0_ 진단 전 / 1_ 진단 후 / 2_ 메모 저장 완료 / 3_ 진단 결과 + 메모 저장 완료
    {
      id: 'id1',
      url: '/images/brains/61.jpg',
      caption: '환자번호 0001',
      age: '27',
      date: '2021-05-10',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id2',
      url: '/images/brains/423.jpg',
      caption: '환자번호 0002',
      age: '25',
      date: '2021-09-23',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id3',
      url: '/images/brains/738.jpg',
      caption: '환자번호 0003',
      age: '36',
      date: '2021-07-17',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id4',
      url: '/images/brains/1091.jpg',
      caption: '환자번호 0004',
      age: '45',
      date: '2020-11-12',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id5',
      url: '/images/brains/1557.jpg',
      caption: '환자번호 0005',
      age: '58',
      date: '2021-09-09',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id6',
      url: '/images/brains/1623.jpg',
      caption: '환자번호 0006',
      age: '47',
      date: '2021-08-13',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id7',
      url: '/images/brains/1687.jpg',
      caption: '환자번호 0007',
      age: '62',
      date: '2021-08-18',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id8',
      url: '/images/brains/1759.jpg',
      caption: '환자번호 0007',
      age: '77',
      date: '2021-07-07',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id9',
      url: '/images/brains/1809.jpg',
      caption: '환자번호 0009',
      age: '27',
      date: '2021-09-23',
      status: 0,
      bookmark: false,
      mono : ''
    },
    {
      id: 'id10',
      url: '/images/brains/1814.jpg',
      caption: '환자번호 0010',
      age: '29',
      date: '2021-06-29',
      status: 0,
      bookmark: false,
      memo : ''
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