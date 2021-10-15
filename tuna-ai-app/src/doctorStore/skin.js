import { reactive } from 'vue'

const state = reactive({
  images: [
    {
      id: 'id1',
      url: '/images/skins/1.jpg',
      caption: '환자번호 0001',
      date: '2021/03/01',
      age: '25',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id2',
      url: '/images/skins/2.jpg',
      caption: '환자번호 0002',
      date: '2021/03/01',
      age: '25',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id3',
      url: '/images/skins/3.jpg',
      caption: '환자번호 0003',
      date: '2021/03/01',
      age: '75',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id4',
      url: '/images/skins/4.jpg',
      caption: '환자번호 0004',
      date: '2021/03/01',
      age: '65',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id5',
      url: '/images/skins/5.jpg',
      caption: '환자번호 0005',
      date: '2021/03/01',
      age: '25',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id6',
      url: '/images/skins/6.jpg',
      caption: '환자번호 0006',
      date: '2021/03/01',
      age: '30',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id7',
      url: '/images/skins/7.jpg',
      caption: '환자번호 0007',
      date: '2021/03/01',
      age: '35',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id8',
      url: '/images/skins/8.jpg',
      caption: '환자번호 0008',
      date: '2021/03/01',
      age: '50',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id9',
      url: '/images/skins/9.jpg',
      caption: '환자번호 0009',
      date: '2021/03/01',
      age: '55',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
    },
    {
      id: 'id10',
      url: '/images/skins/10.jpg',
      caption: '환자번호 0010',
      date: '2021/03/01',
      age: '55',
      memo: '',
      result: '',
      bookmark: false,
      detect: false,
      detect_image: ''
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

const storeSkin = {
  state,
  getters
}

export default storeSkin