import { axios, api ,api2 ,apiDB } from 'boot/axios'
import { onActivated, onDeactivated, ref, reactive} from 'vue'
import { useRoute } from 'vue-router'

const defaults = {
    "memo":  "메모를 입력하세요",
    "data":  "",
    "bookmark": false,
    "detect":  false,
    "detected_image": ""
  }
  
  async function getList(kind) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
  
    var config = {
      method: 'get',
      url: urls[kind],
      headers: { }
    }
  
    try {
      var res =  await apiDB(config)
      return res.data.data    
    } catch(error) {
      console.log(error);
    }
  }
  
  async function getImage(kind, id) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
  
    var config = {
      method: 'get',
      url: urls[kind] + '?id=' + id,
      headers: { }
    }
    try {
      var res =  await apiDB(config)
      return res.data.data[0]
    } catch(error) {
      console.log(error);
    }
  }
    
  async function saveMemo (kind, _id, text) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
    let patchData = {
        "memo": text.value
    }
  
    var config = {
      method: 'patch',
      url: urls[kind] + '/' +_id, // 조회시 나오는 _id 
      headers: { 
        'Content-Type': 'application/json'
      },
      data : patchData
    };
  
    // 메모 업데이트
    try {
      var res =  await apiDB(config)
      console.log('메모 변경: ', res.data)
    } catch(error) {
      console.log(error);
    }
  }
  
  async function saveBookmark (kind, _id, bookmarkbool) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
    let patchData = {
        "bookmark": bookmarkbool
    }
  
    var config = {
      method: 'patch',
      url: urls[kind] + '/' +_id, // 조회시 나오는 _id 
      headers: { 
        'Content-Type': 'application/json'
      },
      data : patchData
    };
  
    // 메모 업데이트
    try {
      var res =  await apiDB(config)
      console.log('북마크 변경: ', res.data)
    } catch(error) {
      console.log(error);
    }
  }
  
  async function saveDectection (kind, _id, result, detected_image) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
    let patchData = {
        "detect": true,
        "detected_image": detected_image,
        "result": result
    }
  
    var config = {
      method: 'patch',
      url: urls[kind] + '/' +_id, // 조회시 나오는 _id 
      headers: { 
        'Content-Type': 'application/json'
      },
      data : patchData
    };
  
    try {
      var res =  await apiDB(config)
      console.log('진단 여부 변경: ', res.data)
    } catch(error) {
      console.log(error);
    }
  }
  
  async function resetDectection (kind, _id) {
    var urls = {
      'chest': '/xray',
      'brain': '/brain',
      'skin': '/skin'
    }
    let patchData = {
      "result":  "",
      "detect":  false,
      "detected_image": ""
    }
  
    var config = {
      method: 'patch',
      url: urls[kind] + '/' +_id, // 조회시 나오는 _id 
      headers: { 
        'Content-Type': 'application/json'
      },
      data : patchData
    };
  
    try {
      var res =  await apiDB(config)
      console.log('진단 여부 리셋: ', res.data)
    } catch(error) {
      console.log(error);
    }
  }

  const DBs = {
    getList,
    getImage,
    defaults,
    saveMemo,
    saveBookmark,
    saveDectection,
    resetDectection
  }
  export default DBs