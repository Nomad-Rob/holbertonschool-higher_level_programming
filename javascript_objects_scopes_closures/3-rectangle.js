#!/usr/bin/node
// Task 3 - Create an instance method called print()
// that prints the rectangle using the character X:

module.exports = class Rectangle {
  constructor (w = -1, h = -1) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
