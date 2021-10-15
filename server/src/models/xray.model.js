// xray-model.js - A mongoose model
// 
// See http://mongoosejs.com/docs/models.html
// for more of what you can do here.
module.exports = function (app) {
  const modelName = 'xray';
  const mongooseClient = app.get('mongooseClient');
  const { Schema } = mongooseClient;
  const schema = new Schema({
    id: {type: String, default: 'id1'}, // default: 선택
    url: {type: String, default: '/images/xrays/1.jpg'}, 
    caption: {type: String, default: '환자번호 0001'},
    date: {type: String, default:  '2021/03/01'},
    age: {type: String, default:  '55'},
    memo: {type: String, default:  '메모를 작성해 주세요.'},
    result: {type: String, default:  ''},
    bookmark: {type: Boolean, default: false}, // Boolean은 default부분 넣어주는게 좋음.
    detect: {type: Boolean, default: false},
    detected_image: {type: String, default: ''}
  }, {
    timestamps: true
  });

  // This is necessary to avoid model compilation errors in watch mode
  // see https://mongoosejs.com/docs/api/connection.html#connection_Connection-deleteModel
  if (mongooseClient.modelNames().includes(modelName)) {
    mongooseClient.deleteModel(modelName);
  }
  return mongooseClient.model(modelName, schema);
  
};
