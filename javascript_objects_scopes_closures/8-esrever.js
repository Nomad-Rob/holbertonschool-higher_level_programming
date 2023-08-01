#!/usr/bin/node
// Task 8 - Write a function that returns the reversed version of a list:

exports.esrever = function (list) {
    const results = [];
    for (let i = list.length - 1; i >= 0; i--) {
      results.push(list[i]);
    }
    return results;
  };
