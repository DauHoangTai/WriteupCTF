const crypto = require('crypto');

secret = `secret-${crypto.randomUUID}`;
// console.log(secret)

function generateToken(id) {
    return crypto
      .createHmac('sha256', this.secret)
      .update(id.toString())
      .digest('hex');
}

console.log(generateToken(0))