#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
