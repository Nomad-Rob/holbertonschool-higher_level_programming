#!/usr/bin/node
// Task 2 - If w or h is equal to 0 or not a positive integer,
// create an empty object:

module.exports = class Rectangle {
  constructor (w = -1, h = -1) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
