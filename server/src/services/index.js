const users = require('./users/users.service.js');
const brain = require('./brain/brain.service.js');
const skin = require('./skin/skin.service.js');
const xray = require('./xray/xray.service.js');
// eslint-disable-next-line no-unused-vars
module.exports = function (app) {
  app.configure(users);
  app.configure(brain);
  app.configure(skin);
  app.configure(xray);
};
