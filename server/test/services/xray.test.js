const assert = require('assert');
const app = require('../../src/app');

describe('\'xray\' service', () => {
  it('registered the service', () => {
    const service = app.service('xray');

    assert.ok(service, 'Registered the service');
  });
});
