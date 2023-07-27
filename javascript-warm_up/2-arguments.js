#!/usr/bin/node
// Task 2 - Write a script that prints a message
// depending of the number of arguments passed:

const argc = process.argv.length;
const values = ['No argument', 'Argument found', 'Arguments found'];
console.log(values[Math.min(argc - 2, 2)]);
