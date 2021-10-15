// Initializes the `brain` service on path `/brain`
const { Brain } = require('./brain.class');
const createModel = require('../../models/brain.model');
const hooks = require('./brain.hooks');

module.exports = function (app) {
  const options = {
    Model: createModel(app),
    paginate: app.get('paginate')
  };

  // Initialize our service with any options it requires
  app.use('/brain', new Brain(options, app));

  // Get our initialized service so that we can register hooks
  const service = app.service('brain');

  service.hooks(hooks);
};
