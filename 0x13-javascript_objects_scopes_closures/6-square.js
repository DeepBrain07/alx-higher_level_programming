#!/usr/bin/node

const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c = 'X') {
    this.print(c);
  }
}
module.exports = Square;
