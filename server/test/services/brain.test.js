const assert = require('assert');
const app = require('../../src/app');

describe('\'brain\' service', () => {
  it('registered the service', () => {
    const service = app.service('brain');

    assert.ok(service, 'Registered the service');
  });
});
