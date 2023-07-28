#!/usr/bin/node
// Task 11 - Searches the second biggest
// integer in the list of arguments

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] < max) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
