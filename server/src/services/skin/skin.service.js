// Initializes the `skin` service on path `/skin`
const { Skin } = require('./skin.class');
const createModel = require('../../models/skin.model');
const hooks = require('./skin.hooks');

module.exports = function (app) {
  const options = {
    Model: createModel(app),
    paginate: app.get('paginate')
  };

  // Initialize our service with any options it requires
  app.use('/skin', new Skin(options, app));

  // Get our initialized service so that we can register hooks
  const service = app.service('skin');

  service.hooks(hooks);
};
