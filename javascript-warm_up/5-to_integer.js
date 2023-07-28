#!/usr/bin/node
// Task 5 - Print My number: <first argument converted in integer>

const inValue = process.argv[2];
if (isNaN(inValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(inValue));
}
