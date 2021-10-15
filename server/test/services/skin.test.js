const assert = require('assert');
const app = require('../../src/app');

describe('\'skin\' service', () => {
  it('registered the service', () => {
    const service = app.service('skin');

    assert.ok(service, 'Registered the service');
  });
});
