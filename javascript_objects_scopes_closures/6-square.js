#!/usr/bin/node
// Task 6 - Create an instance method called charPrint(c)

const myBase = require('./5-square');

module.exports = class Square extends myBase {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
