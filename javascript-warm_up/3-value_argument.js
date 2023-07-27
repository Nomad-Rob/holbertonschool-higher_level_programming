#!/usr/bin/node
// Task 3 - Write a script that prints the first 
// argument passed to it:

let i = 1;
const values = ['No argument', process.argv[2]];
if (values[1] === undefined) {
  i--;
}
console.log(values[i]);
