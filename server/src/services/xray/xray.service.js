// Initializes the `xray` service on path `/xray`
const { Xray } = require('./xray.class');
const createModel = require('../../models/xray.model');
const hooks = require('./xray.hooks');

module.exports = function (app) {
  const options = {
    Model: createModel(app),
    paginate: app.get('paginate')
  };

  // Initialize our service with any options it requires
  app.use('/xray', new Xray(options, app));

  // Get our initialized service so that we can register hooks
  const service = app.service('xray');

  service.hooks(hooks);
};
