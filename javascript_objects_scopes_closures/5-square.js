#!/usr/bin/node
// Task 5 - Create an instance method called charPrint(c)

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
