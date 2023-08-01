#!/usr/bin/node
// Task 1 - Constructor must take 2 arguments w and h:
// Initialize the instance attribute width with the value of w
// Initialize the instance attribute height with the value of h

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
