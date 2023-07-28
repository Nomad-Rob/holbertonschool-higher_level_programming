#!/usr/bin/node
// Task 8 - Print a square

const x = parseInt(process.argv[2]);

if (!x) { console.log('Missing size'); }

for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
