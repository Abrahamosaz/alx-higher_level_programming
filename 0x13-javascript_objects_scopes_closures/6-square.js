#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
